#variables
name = "soma"
age = 20
salary = 25000.00
#rules 
name ="sriram"
_ade = 21

student_name = "arun"
marks1 = 90

#case sensitive
name = "somachandran"
Name = "sriram"
print(name)
print(Name)

#snake_case ; use_
first_name = "raj"
mobile_number = 1234567890

#multiple variable assignment
a,b,c = 10,20,30
print(a)
print(b)
print(c)

# assign same value to multiple var
x = y = z = 100
print(x)
print(y)
print(z)

#dynamic typing 
value = 10
print(value)

value = "hello"
print(value)

#checking var type - use type()
name = "soma"
age = 20
height = 5.7

print(type(name))
print(type(age))
print(type(height))

#example code 
student_name = "Arun"
student_age = 25
mark_1 = 90
mark2 = 94

print("Student name:", student_name)
print("Student Age:", student_age)
print("Subject 1:", mark_1)
print("Subject Mark 2:", mark2)


#DATATYPES 
#
age = 20 
temperature = -5
print(age,temperature)
print(type(age))

#float
salary = 25000.00
cgpa = 84.7

print(salary,cgpa)
print(type(salary))
# string - use "" or ''

name = "soma"
college = 'KG college'
num = "100"
print(name,college,num)
print(type(name))
#string operation 
first_name = "sri"
last_name = "ram"
print(first_name+" "+last_name)
#repeating
print("hi "*4)

#boolean
light_on = True
is_raining = False
print(type(light_on))

#list
fruit = ["Apple","Banana","Orange"]
print(fruit)
print(type(fruit))
#accessing
num = [10,20,30,40,50]
print(num[0])
print(num[3])
#change a list
num[0] = "s"
print(num)

#tuple
days = ("mon","tue","wed","thu","fri")
print(days)
print(type(days))

#set 
num = {1,2,3,4,5,6,7}
print(num)

values = {1,1,2,2,3,4}
print(values)

#dictionary
student = {
    "name": "arun",
    "age":20,"mark":97
}
print(student)
print(type(student))
#accessing
print(student["age"])
print(student["name"])

#complex
x= 2+4j
print(x)
print(type(x))

#type conversion
#int to float
a=10
print(float(a))
#float to int
b=4.4
print(int(b))
#int to string
num =100
print(str(num))


#user input 
name = input("Enter your name: ")
print("hi",name)

#int input 
age = int(input("Enter your age: "))
print(age)
print(type(age))

#float input
weight = float(input("Enter your weight:"))
print(weight)
print(type(weight))

#area of rectangle
length = float(input("Enter the length:"))
breadth = float(input("Enter the breadth:"))
area = length*breadth
print("Area = ",area)

#multiple input 
a,b,c = map(int,input("Enter 3 numbers: ").split())
print(a+b+c)

#list input
num = list(map(int,input("Enter numbers:").split()))
print(num)