import unittest
from twitter.model import twitter_trends
from twitter.util.location_util import populate_location_map


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        populate_location_map()

    def test_trends(self):
        trends = twitter_trends.trends_by_location()
        print(trends)
        assert len(trends) != 0

    def test_available_trend(self):
        #twitter_trends.available_trend("covid")
        pass


if __name__ == '__main__':
    unittest.main()
