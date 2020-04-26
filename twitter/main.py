import io
import json
import logging

from flask import Flask, render_template, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from twitter.model import twitter_trends
from twitter.model.trend_visualizer import visualize_trends
from twitter.util.utility_functions import trends_to_string_util

app = Flask(__name__)


@app.route("/")
def home():
    trends = twitter_trends.trends_by_location()
    webpage = trends_to_string_util(trends)
    return render_template("home.html", message=webpage)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/<location>.png")
def visualize(location):
    trends = twitter_trends.trends_by_location(woeids=[location])
    fig = visualize_trends(trends)
    output = io.BytesIO()
    FigureCanvas(fig[0]).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.errorhandler(500)
def server_error(e):
    logging.exception('Gagan Mani: An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
