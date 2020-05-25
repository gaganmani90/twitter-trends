import io

from flask import Blueprint, send_file, render_template

from twitter.blueprints.bp_home import raw_chart
from twitter.model import twitter_trends
from twitter.model.trend_visualizer import visualize_trends
from twitter.trends_logger import trends_logger
from twitter.util.location_util import location_from_woeid

chart = Blueprint('chart', __name__,
                  template_folder='templates')


@chart.route("/visualize/<location>")
def visualize(location):
    """
    This reders image/png for a given woeid
    Example: http://0.0.0.0:5000/visualize/2282863
    :param location:
    :return:
    """
    trends_logger.info("visualizing location: " + location_from_woeid(location))
    trends = twitter_trends.trends_by_location(woeids=[location])
    fig = visualize_trends(trends)
    fig = fig[0]
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


@chart.route('/images/<location>')
def images(location):
    """
    Renders image page with title of python chart that is non-interactable
    Example: http://0.0.0.0:5000/images/2282863
    :param location:
    :return:
    """
    place = location_from_woeid(location)
    return render_template("images.html", woeid=location, place=place)


@chart.route('/bar/<location>')
def html_chart(location):
    """
    renders HTML interactable chart for a given woeid
    Example: http://0.0.0.0:5000/bar/2282863
    :param location:
    :return:
    """
    json = raw_chart(location).get_json()
    return render_template('chartjs.html', title=json['title'], volumes=json['volumes'], topics=json['topics'])
