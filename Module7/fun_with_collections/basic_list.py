def make_list():

    list = []
    n = 3
    for i in range(0,n):
        print("Enter number at location", i, ":")
        numbers = int(input())
        list.append(numbers)

    print( "The list is ", list)


def get_input():
    number =  int(input("Enter a number"))

if __name__ == '__main__':
    make_list()
