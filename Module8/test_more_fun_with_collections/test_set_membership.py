import unittest


class TestSet(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(True, False)
    def test_in_set_False(self):
        self.assertEqual(False, True)


if __name__ == '__main__':
    unittest.main()
