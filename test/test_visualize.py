import unittest

from twitter.model import twitter_trends
from twitter.model.trend_visualizer import visualize_trends
from twitter.util.location_util import populate_location_map


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        populate_location_map()

    def test_visualize_trend(self):
        #trends = twitter_trends.trends_by_location(woeids=get_location_map().keys())
        trends = twitter_trends.trends_by_location()
        figures = visualize_trends(trends)
        assert len(figures) != 0
        figures[0].canvas.draw_idle()


if __name__ == '__main__':
    unittest.main()
