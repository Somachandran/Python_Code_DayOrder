# # Exception Handling
# # try
# try:
#     num = int(input("Enter s number: ")) 
#     print(num)
# except:
#     print("Invalid input")

# #ATM 
# balance = 1000
# try:
#     amount = int(input("Enter amount: "))
#     print(balance / amount)
# except:
#     print("Somathing went wrong!")

# #Handling Specific Exceptions
# try:
#     num = int(input("Enter number: "))
#     result = 10 / num
#     print(result)

# except ValueError:
#  print("Please enter only number: ")
# except ZeroDivisionError:
#    print("Cannot divide by Zero.") 
# finally:
#    print("Program Finished.")

# #raise
# age = int(input("Enter age: "))
# if age < 18:
#     raise ValueError("Age must be 18 or above")
# print("Eligible")
# #ATM
# balance = 500
# if balance < 1000:
#     raise Exception("Minimum balance required")

# #Custom Exception
# class AgeError(Exception):
#     pass
# age = int(input("Enter age: "))
# if age < 18:
#     raise AgeError("You are too young")
# print("Access granted")

# # Student Registration System
# class AgeError(Exception):
#    pass
# class Mark(Exception):
#    pass
# class Name(Exception):
#    pass
# try:
#     name = str(input("Enter your name: "))
#     if not name.isalpha():
#        raise Name("Only give letters as input , number and others are not allowed")
#     age = int(input("Enter your Age: "))
#     if not age >= 18:
#      raise AgeError("Age must be 18 or above")
#     mark = int(input("Enter your mark: "))
#     if mark < 1 or mark > 101:
#        raise Mark("Marks should be in 1 to 100")

# except AgeError as e:
#    print(e)
# except Mark as e:
#    print(e)
# except ValueError:
#    print("Age and mark must be a number,please enter only numeric values")
# except Name as e:
#    print(e)
# else:
#    print("Registration Successful")
#    print("Name: ",name)
#    print("Age: ",age)
#    print("Mark: ",mark)
# finally:
#    print("Program Ended")