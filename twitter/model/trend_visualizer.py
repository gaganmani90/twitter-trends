import matplotlib.pyplot as plt

from twitter.data import cache
from twitter.util.constants import GRAPH
from twitter.util.utility_functions import get_location_from_woeid


def _visualize_trend(location, trend):
    topic = [x.name for idx, x in enumerate(trend[:20])]
    volume = [x.volume for idx, x in enumerate(trend[:20])]
    figure = _get_graph_figure(labels=['volume', 'trends'], values=[topic, volume], title=location)
    return figure


def _get_graph_figure(labels=[], values=[], title="My Graph"):
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)
    plt.barh(values[0], values[1])
    axis = plt.gca()
    axis.invert_yaxis()
    #axis.get_xaxis().get_major_formatter().set_useOffset(False)
    plt.tight_layout()
    # plt.savefig("static/images/"+title)
    # plt.show()
    return plt.gcf()


def visualize_trends(trends: dict):
    figures = []
    for woeid, trend in trends.items():
        key = woeid + "_" + GRAPH
        if cache.get_cache(key):
            figures.append(cache.get_cache(key))
        else:
            graph = _visualize_trend(get_location_from_woeid(woeid), trend)
            cache.update_cache(key, graph)
            figures.append(graph)
    return figures
