import unittest

from twitter.data.database.connect import DBOperations, TABLE_TREND


@unittest.skip("skip")
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        conn = DBOperations.getConnection()
        assert conn is not None

    @classmethod
    def tearDown(self) -> None:
        DBOperations.close()

    def test_something(self):
        # available_trend()
        assert DBOperations.row_count(TABLE_TREND) == 0
        DBOperations.create_trend_table()


if __name__ == '__main__':
    unittest.main()
