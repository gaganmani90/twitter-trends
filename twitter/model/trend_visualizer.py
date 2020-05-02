import logging

import matplotlib.pyplot as plt

from twitter.util.location_util import get_location_from_woeid

def _visualize_trend(location, trend):
    topic = [x.name for idx, x in enumerate(trend[:20])]
    volume = [x.volume for idx, x in enumerate(trend[:20])]
    figure = _get_graph_figure(labels=['volume', 'trends'], values=[topic, volume], title=location)
    return figure


def _get_graph_figure(labels=[], values=[], title="My Graph"):
    plt.clf() # clear
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)
    plt.barh(values[0], values[1])
    axis = plt.gca()
    #axis.invert_yaxis()
    plt.tight_layout()
    # plt.savefig("static/images/"+title)
    # plt.show()
    return plt.gcf()


def visualize_trends(trends: dict):
    logging.info("Start: visualizing trends, trends length: {}".format(len(trends)))
    logging.debug(trends)
    figures = []
    for woeid, trend in trends.items():
            graph = _visualize_trend(get_location_from_woeid(woeid), trend)
            figures.append(graph)
    return figures
