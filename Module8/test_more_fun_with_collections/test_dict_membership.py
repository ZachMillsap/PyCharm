import unittest
def in_dict(dict,value):

   for dict_value in test_dict.values():

       if(dict_value == value):

           return True

   return False



if __name__ == "__main__":

   test_dict = {"A" : 1, "B" : 2, "C" : 3}

   Test1 = in_dict(test_dict,1)

   print("The Result for Calling function with test_dict, 1 is :", Test1)

   Test2 = in_dict(test_dict,0)

   print("The Result for Calling function with test_dict, 0 is :", Test2)

