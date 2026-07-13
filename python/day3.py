# Operators
# Arithmetic Operators

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulo:", a % b)
print("Floor Division:", a // b)
print("Exponential:", a ** b)
price = 12
quantity = 5
total = price * quantity
print(total)

#comparison o
a= 13
b=33
print(a>b)
print(a<b)
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)
age = 18
print(age >= 18)

#logical o
a = True
b = False
print(a and b)
print(a or b)
print(not b)
age = 20
licence = True
print(age >= 18 and licence)

#bitwise o
a = 10
b = 4 
print(a&b)
print(a|b)
print(~a)
print(a^b)
print(a>>2)
print(a<<2)

#assignment o
a =10 
b= a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b /= a
print(b)
salary = 10000
salary += 2000
print(salary)

#identity o
a =10
b = 20
c = a
print(a is not b)
print(a is c)

#membership o
x = 24
y = 20
my_list = [10,20,30,40,50]
if (x not in my_list):
    print("x is not present in given list")
else:
    print("x is present in given list")
if (y in my_list):
    print("y is  present in given list")
else:
    print("y is  not present in given list")

name = "python"
print("p" in name)

#ternary o
a,b = 10,20
min = a if a < b else b
print(min)

#calculator program
a = int(input("Enter the  1st number:"))
b = int(input("Enter the 2nd number:"))
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Mulatiplcation:",a*b)
print("Division:",a/b)
print("Remainder:",a%b)