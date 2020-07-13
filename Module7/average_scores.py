def average_scores(*args, **kwargs):
    # Use *args for average calculation
    avg = sum(args)/len(args)
    print("GPA avg :", avg)

    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    # return


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
    print(average_scores(5, 0, 3, 2, 5, name='Zach', gpa='2.0', course='Python'))
    print(average_scores(1, 2, 3, 4, name='Tim', gpa='3.4', course='Python'))

# Result: name = M gpa = 3.2 course = Python with current average 30.0
