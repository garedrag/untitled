#!/usr/bin/env python3
class User:
    def __init__(self, name, day, month):
        self.name = name
        self.day = day
        self.month = month

    def months(self, month):
      try:
        list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                'november', 'december']
        month = self.month.lower()
        while month in list:
            print(month)
            return list.index(month)
            break
        month = int(month)
        print(month)
        print(type(month))
        while month in range(0, 13):
            self.month = month
            return self.month
        else:
            print('This is not month')
            print(type(month))
            quit()
      except ValueError:
           print('This is not month')
    def days(self, day):
      try:
        day = self.day
        while int(day) in range (0, 32):
            return int(day)
        else:
            print('It is not right day')
            quit()
      except ValueError:
          print('This is not right day')

    def astro(self, znak):
        self.znak = znak
        if month == 1 and day in range (20, 31) or month == 2 and day in range (1, 19):
            znak = 'aquarius'
        elif month == 2 and day in range(19, 31) or month == 3 and day in range (1, 19):
            znak = 'pisces'


obj1 = User(
    input("Input You Name: "),
    input("Day of birthday: "),
    input("Month of birthday: "))
obj1.month = obj1.months(obj1.month)
obj1.day = obj1.days(obj1.day)
print (obj1.name, obj1.day, obj1.month)
astro1 = Astro()
print(astro)


















