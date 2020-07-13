def write_to_file(args, kwargs):
    f = open('student_info.txt', 'w')
    f.write(kwargs)
    tuple = (args)
    input_list = tuple
    f.writelines(input_list)
    f.close()

def get_student_info(*args, **kwargs):

    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        kwargs = str(kwargs)
    scores = []
    line = input('Enter the list of scores. Enter done to end\n')
    while(line != 'done'):
        scores.append(tuple(line.split()))
        line = input()
    args = str(scores)
    write_to_file(args, kwargs)

def read_from_file():
    import os as os

    file_dir = os.path.dirname(__file__)
    file_name = "student_info.txt"
    f = open(os.path.join(file_dir, file_name), "r")
    line1 = f.read()
    print(line1)
    f.close()

if __name__ == '__main__':
    get_student_info(name = 'zach')
    get_student_info(name = 'steven')
    get_student_info(name = 'tim')
    get_student_info(name = 'rachel')
    read_from_file()
    input("Press any key to end")
