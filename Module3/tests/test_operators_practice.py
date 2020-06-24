import unittest

class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        a = 7
        b = -2
        self.assertTrue(a == b)
    def test_not_equals(self):
        a = 7
        b = -2
        self.assertFalse(a != b)
    def test_greater_than(self):
        a = 7
        b = -2
        self.assertFalse(a > b)
    def test_less_than(self):
        a = 7
        b = -2
        self.assertTrue(a < b)
    def test_greater_than_or_equal(self):
        a = 7
        b = -2
        self.assertFlase(a >= b)
    def test_less_than_or_equal(self):
        a = 7
        b = -2
        self.assertTrue(a <= b)

if __name__ == '__main__'
    unittest.main()
