# #Decorators
# def decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper
# @decorator
# def greet():
#     print("Hello Friend!")
# greet()

# #Logging Function Calls
# def logger(func):
#     def wrapper():
#         print("Function is being called")
#         func()
#         print("Function execution completed")
#     return wrapper
# @logger
# def welcome():
#     print("Welcome to python")
# welcome

# #Decorator with Arguments
# def decorator(func):
#     def wrapper(name):
#         print("Before")
#         func(name)
#         print("After")
#     return wrapper
# @decorator
# def greet(name):
#     print(f"Hello {name}")
# greet("Juinth")

# #Generic Decorator (*args, **kwargs)
# def de(f):
#     def wrapper(*args,**kwargs):
#         print("Before")
#         result = f(*args,**kwargs)
#         print("After")
#         return result
#     return wrapper
# @de
# def add(a,b):
#     return a+b
# print(add(10,20))

# # Task Create a decorator called check_login
# def decorator(func):
#     def wrapper():
#         print("Checking login..")
#         func()
#         print("Access Granted")
#     return wrapper
# @decorator
# def welcome():
#     print("Welcome User")
# welcome()