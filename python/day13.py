# #packages and modules
# import math
# print(math.sqrt(25))

# from math import sqrt
# print(sqrt(35))

# #multiple im
# from math import sqrt,factorial
# print(sqrt(64))
# print(factorial(5))

# #im as 
# import math as m
# print(m.sqrt(49))

# #math module
# import math

# print(math.sqrt(25))#sqrt

# print("power:",math.pow(2,3))#pow

# print("Factorial:",math.factorial(6))

# print("Rounds up:",math.ceil(4.2))

# print("Rounds down:",math.floor(4.8))

# print("pi value:",math.pi)

# #area of circle
# import math
# radius = 7
# area = math.pi * radius *radius
# print(area)

# #Random module
# import random as r

# print("Random int:",r.randint(1,12))

# names = ["ram","soma","sri","naveen"]
# print("choose one item:",r.choice(names))

# nums = [1,2,3,4,5,6,7]
# r.shuffle(nums)
# print(nums)

# #lottery winner
# import random
# players = ['A','B','C','D','E']
# winner = random.choice(players)
# print("winner:",winner)

# #Datetime module
# import datetime as dt

# today = dt.date.today()
# print("Current Date:",today)

# now = dt.datetime.now()
# print("Current date and time:",now)

# #create date
# d= dt.date(2006,2,4)
# print(d)

# #extract year ,month ,day
# import datetime
# today = datetime.date.today()
# print(today.year)
# print(today.month)
# print(today.day)

# #Calculate age
# import datetime
# birth_year = 2006
# current_year = datetime.date.today().year
# age = current_year - birth_year
# print("Your age is:",age)

# #time module
# import time

# print("Start...")
# time.sleep(4)
# print("End")

# #practice programs
# import random
# print("Random number=",random.randint(1,100))#r 1 to 100
# num = [11,22,33,44,55]
# random.shuffle(num)
# print(num)

# import math
# print(math.factorial(5))
# print(math.sqrt(7))

# radius = 6
# area = math.pi * radius *radius
# print(area)

# import datetime
# print(datetime.datetime.today())

# t = datetime.datetime.today()
# print(t.year)
# print(t.month)
# print(t.day)

# #Random password
# import random

# ran = "abcdefghijklmnopqrstuvwxyz!@#$%^&*1234567890"
# password = ""
# for i in range(8):
#     password += random.choice(ran)

# print("Password is:",password)