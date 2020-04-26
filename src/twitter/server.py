from flask import Flask

from twitter import twitter_trends

app = Flask(__name__)


@app.route("/")
def hello():
    trends, size = twitter_trends.trends_by_location()
    return "".join(["Gagan <br/>", "<br/>".join(map(str, trends))])


if __name__ == "__main__":
    app.run()
