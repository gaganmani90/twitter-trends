import io

from flask import Blueprint, send_file

from twitter.model import twitter_trends
from twitter.model.trend_visualizer import visualize_trends
from twitter.trends_logger import trends_logger
from twitter.util.location_util import location_from_woeid

chart = Blueprint('chart', __name__,
                   template_folder='templates')


@chart.route("/visualize/<location>")
def visualize(location):
    trends_logger.info("visualizing location: " + location_from_woeid(location))
    trends = twitter_trends.trends_by_location(woeids=[location])
    fig = visualize_trends(trends)
    fig = fig[0]
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')
