from flask import Flask, render_template
import logging

from twitter import twitter_trends

app = Flask(__name__)


@app.route("/")
def home():
    trends, size = twitter_trends.trends_by_location()
    webpage = "".join(["Gagan \n", "\n".join(map(str, trends))])
    #return render_template("index.html", message=webpage)
    return render_template("home.html", message=webpage)


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(500)
def server_error(e):
    logging.exception('Gagan Mani: An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
