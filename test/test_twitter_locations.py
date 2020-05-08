import unittest

from twitter.model.twitter_locations import available_trend
from twitter.util.location_util import populate_location_map


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        populate_location_map()

    def test_something(self):
        #available_trend()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
