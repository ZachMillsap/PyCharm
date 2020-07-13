import unittest
from datetime import datetime, timedelta


def half_birthday(date):
    half_birthday_date = date + timedelta(days=180)
    return half_birthday_date


birthday = datetime(2020,2,3)
print(half_birthday(birthday))

if __name__ == '__main__':
    unittest.main()
