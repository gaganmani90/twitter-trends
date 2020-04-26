import unittest
from twitter.model import twitter_trends


class Test(unittest.TestCase):

    def test_trends(self):
        trends = twitter_trends.trends_by_location()
        print(trends)
        assert len(trends) != 0
        twitter_trends.print_user_details("shivani0811")

    def test_available_trend(self):
        #twitter_trends.available_trend("covid")
        pass


if __name__ == '__main__':
    unittest.main()
