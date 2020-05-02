import unittest

from twitter.util.location_util import *


class MyTestCase(unittest.TestCase):
    def test_populate_location_map(self):
        populate_location_map()
        self.assertIsNotNone(location_to_woeid_map())
        self.assertIsNotNone(woeid_to_location_map())
        self.assertIsNotNone(child_models(1))
        self.assertEqual(0, len(child_models(1)))
        self.assertIsNotNone(location_models())
        self.assertIsNotNone(location_from_woeid(1))


if __name__ == '__main__':
    unittest.main()
