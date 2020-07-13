def in_set():
    my_set = {1,1,2,3,4}
    user_input = int(input("Enter a value to check"))

    for user_input in my_set:
        return True
    else:
        return False
if __name__ == "__main__":

    in_set()


