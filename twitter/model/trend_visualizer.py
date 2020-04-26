import matplotlib.pyplot as plt

from twitter.util.utility_functions import get_location_from_woeid


def _visualize_trend(location, trend):
    topic = [x.name for idx, x in enumerate(trend[:20])]
    volume = [x.volume for idx, x in enumerate(trend[:20])]
    figure = _get_graph_figure(labels=['volume', 'trends'], values=[topic, volume], title=location)
    # plt.savefig('trends.png')
    return figure


def _get_graph_figure(labels=[], values=[], title="My Graph"):
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title)
    plt.barh(values[0], values[1])
    plt.gca().invert_yaxis()
    plt.tight_layout()
    #plt.savefig("static/images/"+title)
    #plt.show()
    return plt.gcf()


def visualize_trends(trends: dict):
    figures = []
    for woied, trend in trends.items():
        figures.append(_visualize_trend(get_location_from_woeid(woied), trend))
    return figures
