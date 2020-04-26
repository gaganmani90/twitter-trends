import unittest
from src.twitter import twitter_trends


class Test(unittest.TestCase):
    def test_trends(self):
        print(str(twitter_trends.trends()));


if __name__ == '__main__':
    unittest.main()