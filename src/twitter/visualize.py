import matplotlib.pyplot as plt


def visualize_trend(trends):
    topic = [x.name for idx, x in enumerate(trends[:10])]
    volume = [x.volume for idx, x in enumerate(trends[:10])]
    plt.title("Twitter Trends in India")
    plt.xlabel('volume')
    plt.ylabel('trends')
    # plt.plot(volume, topic)
    plt.barh(topic, volume)
    plt.savefig('trends.png')
    plt.gca().invert_yaxis()
    plt.show()
