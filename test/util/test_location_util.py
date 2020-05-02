import unittest

from twitter.util.location_util import populate_location_map


class MyTestCase(unittest.TestCase):
    def test_populate_location_map(self):
        location_to_woeid, woeid_to_location = populate_location_map()
        self.assertIsNotNone(location_to_woeid)
        self.assertIsNotNone(woeid_to_location)


if __name__ == '__main__':
    unittest.main()
