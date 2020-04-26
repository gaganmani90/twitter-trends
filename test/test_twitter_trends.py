import unittest
from src.twitter import twitter_trends


class Test(unittest.TestCase):

    def test_trends(self):
        trends, size = twitter_trends.trends_by_location()
        print("\n".join(map(str, trends)))
        print(size)
        assert len(trends) != 0
        twitter_trends.print_user_details("shivani0811")


if __name__ == '__main__':
    unittest.main()
