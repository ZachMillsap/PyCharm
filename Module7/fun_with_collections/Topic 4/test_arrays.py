import array as arr

def sort_array(array_list):
    array_list.reverse()
    return array_list

def search_array(array_list): # will return the index of the object in the list or a -1 if the item is not found
    x = int(input(print("What index would you like to see?")))
    print(array_list.index(x))


if __name__ == '__main__':
    array_list = arr.array('d',[1,2,3,4,5])
    search_array(array_list)
    sort_array(array_list)
    print(array_list)   #Returned because I needed to show that the list was reversed

