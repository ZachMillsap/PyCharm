import unittest
def search_array(array_list): # will return the index of the object in the list or a -1 if the item is not found
    x = int(input(print("What index would you like to see?")))
    print(array_list.index(x))

class TestSearchArray(unittest.TestCase):

    def test_search_array(self):
        self.assertEqual(search_array(1))
        self.assertNotEqual(search_array(1))


if __name__ == '__main__':
    unittest.main()
