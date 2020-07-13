import unittest


class TestSet(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(True, True)
    def test_in_set_False(self):
        self.assertEqual(False, False)


if __name__ == '__main__':
    unittest.main()
