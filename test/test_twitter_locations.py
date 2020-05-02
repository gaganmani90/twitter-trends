import unittest

from twitter.model.twitter_locations import available_trend


class MyTestCase(unittest.TestCase):
    def test_something(self):
        available_trend()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
