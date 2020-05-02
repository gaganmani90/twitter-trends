import io
import logging

import matplotlib
from flask import Flask, render_template, send_file

from twitter.util.location_util import *

matplotlib.use('Agg')

from twitter.model import twitter_trends
from twitter.model.trend_visualizer import visualize_trends
from twitter.util.utility_functions import trends_to_string_util

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[Twitter Trends] ")


@app.before_first_request
def setup():
    logger.info("Initializing ...")
    populate_location_map()


@app.route("/")
def home():
    locations = woeid_to_location_map()
    locations_by_parent = location_models()
    # expensive call (do not uncomment)
    # trends = twitter_trends.trends_by_location(locations.keys())

    trends = twitter_trends.trends_by_location()
    webpage = trends_to_string_util(trends)
    return render_template("home.html", message=webpage, map=locations, locations_by_parent=locations_by_parent)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/images/<location>')
def images(location):
    place = location_from_woeid(location)
    return render_template("images.html", woeid=location, place=place)


@app.route("/visualize/<location>")
def visualize(location):
    logger.info("visualizing location: " + location_from_woeid(location))
    trends = twitter_trends.trends_by_location(woeids=[location])
    fig = visualize_trends(trends)
    fig = fig[0]
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == "__main__":
    app.run(port=8080, debug=False)
