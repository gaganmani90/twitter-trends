import unittest

from twitter import twitter_trends
from twitter.visualize import visualize_trend


class MyTestCase(unittest.TestCase):

    def test_visualize_trend(self):
        trends, size = twitter_trends.trends_by_location()
        visualize_trend(trends)


if __name__ == '__main__':
    unittest.main()
