import matplotlib.pyplot as plt


def visualize_trend(trends):
    topic = [x.name for idx, x in enumerate(trends[:20])]
    volume = [x.volume for idx, x in enumerate(trends[:20])]
    plt.title("Twitter Trends in India")
    plt.xlabel('volume')
    plt.ylabel('trends')
    # plt.plot(volume, topic)
    plt.barh(topic, volume)
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.savefig('trends.png')
    #plt.show()
    return plt.gcf()
