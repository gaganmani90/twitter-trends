import logging

import matplotlib
from flask import Flask, render_template
from flask_jsglue import JSGlue

from twitter.blueprints.bp_about import about
from twitter.blueprints.bp_home import home
from twitter.blueprints.bp_image import chart
from twitter.trends_logger import trends_logger
from twitter.util.location_util import *

matplotlib.use('Agg')

app = Flask(__name__)
app.register_blueprint(chart)  # produce chart
app.register_blueprint(home)  # home page
app.register_blueprint(about)  # about page
jsglue = JSGlue(app)


@app.before_first_request
def setup():
    logging.basicConfig(level=logging.INFO)
    trends_logger.info("Initializing ...")
    populate_location_map()



@app.errorhandler(500)
def server_error(e):
    trends_logger.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == "__main__":
    app.run(port=8080, debug=False)
