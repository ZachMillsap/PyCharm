MAX = 10
MIN = 0
y = 5
x = 20

if y > MAX:
    print('Y is greater than 10')
elif y < MIN:
    print('Y is less than 0')
else:
    print('Y is neither more than 10 or less than 0')

if MIN < x < MAX:
    print('X is between 0 and 10')
elif MIN != x != MAX:
    print('x does not equal 10 or 0')

if MIN <= x <= MAX and x != MAX:
    print('X is between 0 and 10')

if MIN < x < MAX and x !=MAX:
    print('X is between 0 and 9')
