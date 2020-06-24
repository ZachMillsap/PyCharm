def average_scores():
    last_name = input('What is your last name?')
    first_name = input('What is your last name?')
    age = input('What is your age?')
    score1 = input('Enter a score (1-100)')
    score2 = input('Enter another score (1-100)')
    score3 = input('Enter your last score (1-100)')
    average_scores = ((score1+score2+score3)/3)
    average_scores = average()

    print(last_name)
    print(first_name)
    print(age)
    print(average_scores)

    return  # variable
