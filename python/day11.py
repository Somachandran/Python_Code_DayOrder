# #Functions
# def Greet():
#     print("Welcome Friend...")

# #call
# Greet()

# #parameters
# def greet(name):
#     print("Hello",name)
# greet("soma")
# #multiple p
# def add(a,b):
#     print(a+b)
# add(4,3)

# #return s
# def add(a,b):
#     return(a+b)
# result = add(10,20)
# print(result)

# #Default arguments
# def order(item="tea"):
#     print("Order:",item)
# order()
# order("coffee")
# #keyword a
# def student(name,age):
#     print(name,age)
# student(age=20,name="soma")
# #positional a
# def student(name,age):
#     print(name,age)
# student("soma",20)
# #Arbitrary a
# def numbers(*args):
#     print(args)
# numbers(1,2,3,4,4)
# #keyword arbitrary a
# def details(**kwargs):
#     print(kwargs)
# details(name = "sriram",age = 22)

# def student(**data):
#     for key,value in data.items():
#         print(key,value)
# student(name="arun",age=21,city="Annur")

# #lamda f
# square = lambda x:x*x
# print(square(5))
# #with multiple args
# add = lambda x,y:x+y
# print(add(3,7))

# #Nested F
# def outer():
#     print("Outter funtions")
#     def inner():
#         print("Inner funtions")

#     inner()
# outer()

# #real ex
# def login(username , password):
#     if username == "soma" and password == "1234":
#         return"Login successful"
#     return"Invalid User"
# print(login("soma","1234"))
# print(login("arun","1234"))

# #tasks
# def bank(balance,withdraw):
#     if balance >= withdraw:
#         rm = balance - withdraw
#         print("withdraw successfully")
#         print("Remaining amount=",rm)
#     else:
#         print("Insufficient balance.")

# bank(5000 ,1000)

# def largestnum(*num):
#     for nums in num:
#         print(max(nums))
            
# largestnum([12,45,78,23,9])

# def vowel_count(text):
#     vowels,consonants = 0,0
#     for texts in text:
#         if texts in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
#     #return vowels,consonants

#     print("vowels:",vowels)
#     print("consonants:",consonants)

# print(vowel_count("python"))

# def calculater(a =2,b = 4):
#     a = int(input("enter num 1:"))
#     b = int(input("enter num 2:"))
#     opt = input("Enter a operator:")
#     if opt == "+":
#        return(a+b) 
#     elif opt =="-":
#         return(a-b)
#     elif opt =="/":
#         return(a/b)
#     else:
#         return("Invalid option.")
# print(calculater(2,5))    