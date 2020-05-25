import matplotlib.pyplot as plt

from twitter.model import twitter_trends
from twitter.trends_logger import trends_logger
from twitter.util.location_util import location_from_woeid


def _visualize_trend(location, trend):
    trends_logger.info("Visualizing {}".format(location))
    topic = [x.name for idx, x in enumerate(trend[:20])]
    volume = [x.volume for idx, x in enumerate(trend[:20])]
    figure = _get_graph_figure(labels=['volume', 'trends'], values=[topic, volume], title=location)
    return figure


def _get_graph_figure(labels=[], values=[], title="My Graph"):
    plt.clf()  # clear
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)
    plt.barh(values[0], values[1])
    axis = plt.gca()
    axis.invert_yaxis()
    plt.tight_layout()
    # plt.savefig("static/images/"+title)
    # plt.show()
    return plt.gcf()


def visualize_trends(trends: dict):
    trends_logger.info("Start: visualizing trends, trends length: {}".format(len(trends)))
    trends_logger.debug(trends)
    figures = []
    for woeid, trend in trends.items():
        graph = _visualize_trend(location_from_woeid(woeid), trend)
        figures.append(graph)
    trends_logger.info("End: visualizing trends, trends length: {}".format(len(trends)))
    return figures


def graph_labels_by_woeid(woeid: int, limit=20):
    """

    :param woeid: location geo id
    :param limit: limit on top trending topics (50 max)
    :return:
    """
    trend = twitter_trends._trend_for_one_location(woeid)
    topics = [x.name for idx, x in enumerate(trend[:limit])]  # label
    volumes = [x.volume for idx, x in enumerate(trend[:limit])]
    title = location_from_woeid(woeid)
    return topics, volumes, title
