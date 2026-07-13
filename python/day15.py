# #basic oop
# # class 
# class student:
#     pass
# #object
# class student:
#     pass
# s1 = student()
# s2 = student()
# print(s1)
# print(s2)

# class student:
#     name = "soma"
#     age = 20
# s1 = student()
# print(s1.name)
# print(s1.age)

# #methods
# class student:
#     def display(self):#current object
#         print("Hello Student")
# s1 = student()
# s1.display()
# class student:
#     def set_name(self,name):
#         self.name = name
#     def show(self):
#         print(self.name)
# s1 = student()
# s2 = student()
# s1.set_name("soma")
# s2.set_name("Junith")
# s1.show()
# s2.show()

# #constructor
# class student:
#     def __init__(self):
#         print("Object created")
# s1 = student()
# #with parameter
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1 = student("ram",21)
# print(s1.name)
# print(s1.age)

# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =age
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# s1 = student("soma",20)
# s2 = student("Junith",21)
# s1.display()
# print()
# s2.display()
        
# #practice 
# #car
# class car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
#     def display(self):
#         print("Car name:",self.brand)
#         print("Color:",self.color)
# c1 = car("BMW","blue")
# c1.display()