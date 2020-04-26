import unittest
from twitter import twitter_trends
from twitter.twitter_trends import Trend


class Test(unittest.TestCase):

    def test_trends(self):
        trends, size = twitter_trends.trends_by_location()
        print("\n".join(map(str, trends)))
        print(size)
        assert len(trends) != 0
        twitter_trends.print_user_details("shivani0811")

    def test_available_trend(self):
        #twitter_trends.available_trend("covid")
        pass


if __name__ == '__main__':
    unittest.main()
