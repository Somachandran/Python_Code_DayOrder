# # Method Overloading
# class test:
#     def show(self):
#         print("First")
#     def show(self,name):
#         print("Hello",name)
# o = test()
# o.show("Soma")

# class calculator:
#     def add(self,a,b,c=0):
#         return a + b+ c
# o = calculator()
# print(o.add(2,3))
# print(o.add(2,3,4))

# #Method Overriding
# class animal:
#     def sound(self):
#         print("Animal makes a sound")
# class dog(animal):
#     def sound(self):
#         print("dog barks")
# d= dog()
# d.sound()

# class employee:
#     def work(self):
#         print("Employee works")
# class developer(employee):
#     def work(self):
#         print("Developer writes code")
# o = developer()
# o.work()

# #super()
# class person:
#     def __init__(self,name):
#         self.name = name
# class student(person):
#     def __init__(self,name,course):
#         super().__init__(name)
#         self.course = course
# s = student("Soma","Python")
# print(s.name)
# print(s.course)

# class animal:
#     def sound(self):
#         print("Animal sound")
# class dog(animal):
#     def sound(self):
#         super().sound()
#         print("Dog barks")
# d = dog()
# d.sound()

# #Static Methods
# class math:
#     @staticmethod
#     def add(a,b):
#         return a+ b
# print(math.add(10,20))

# #Temperature converter
# class converter:
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return (c * 9/5) + 32
# print(converter.celsius_to_fahrenheit(35))


# #Class Method
# class student:
#     school = "KG School"
#     @classmethod
#     def get_school(cls):
#         return cls.school
# print(student.get_school())

# #Change Class Variable
# class student:
#     school = "KG School"
#     @classmethod
#     def change_school(cls,new_name):
#         cls.school = new_name

# student.change_school("Amala School")
# print(student.school)
