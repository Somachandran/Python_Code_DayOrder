# #opps concepts
# #Encapsulation
# class bank:
#     def __init__(self):
#      self.__balance = 10000
#     def show_balance(self):
#      print(self.__balance)
# b = bank()
# b.show_balance()
# #Abatration
# from abc import ABC,abstractmethod
# class vehicle(ABC):
#   @abstractmethod
#   def start(self):
#     pass
  
# class car(vehicle):
#  def start(self):
#     print("Car started")
# c= car()
# c.start()

# #inheritance
# class animal:
#   def eat(self):
#     print("Eating")
# class dog(animal):
#   pass
# d = dog()
# d.eat()

# #polmorphism
# class dog:
#   def sound(self):
#     print("Barks")
# class cat:
#   def sound(self):
#     print("Meow")
# animals = [dog(),cat()]
# for a in animals:
#   a.sound()

# #ex
# from abc import ABC,abstractmethod
# class payment(ABC):#Parent class
#   @abstractmethod
#   def pay(self):#abstration
#     pass
# class upi(payment):#Child class
#   def pay(self):#polymorphism
#     print("Paid using UPI")
# class creditCard(payment):#Child class
#   def pay(self):#polymorphism
#     print("Paid using Credit Card")
# p1 = upi()
# p2 = creditCard()
# p1.pay()#object
# p2.pay()

# #Employee management system
# class employee:
#   def emp_details(self,name,age):
#     self.name = name
#     self.age = age
#     print("Employee Name:","Ram")
#     print("Employee Age:",self.age)
# from abc import ABC, abstractmethod
# class payment(ABC):
#   @abstractmethod
#   def pay(self):
#     pass
# class gpay(payment):
#   def pay(self):
#     print("Payment was made in Gpay..")
# class salary(employee,gpay):
#   def sal(self):
#     self.amt = 50000
#     print("Salary:",self.amt)
# emp = salary()
# emp.sal()
# emp.emp_details("edgf",45)
# emp.pay()