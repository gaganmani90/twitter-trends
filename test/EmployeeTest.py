import unittest

from src.Employee import Employee


class MyTestCase(unittest.TestCase):
    def test_something(self):
        employee = Employee("Gagan",31)
        self.assertEqual(employee.name, "Gagan")
        self.assertEqual(employee.age, 31)


if __name__ == '__main__':
    unittest.main()
