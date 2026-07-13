#conditional statements
#if
age = 20
if age >= 18 :
    print("Eligible to vote. ")

#If-else
age = int(input("Enter your age:"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote .")

mark = int(input("Enter your Mark:"))
if mark > 90:
    print("Grade A")
elif mark > 70:
    print("Grade B")
elif mark > 50:
    print("Grade C")
elif mark > 35:
    print("pass.... ")
else:
    print("fail...")

    #nested if
age = 20
has_id = True

if age >= 18:
      if has_id:
            print("Entry allowed")
      else:
            print("ID required")
else:
        print("under age")

    #Comparison Operators
num = 10
if num == 10:#==
      print("EQUAL.")
age = 25
salary = 40000

if age > 18 and salary > 30000:# and
    print("Eligible")

marks = 40
sports = True

if marks >= 35 or sports:#or
    print("Selected.")

    is_raining = False

    if not is_raining: #not
        print("Go outside")
#short-hand if
age = 16
result = "Adult" if age >= 18 else "Minor"
print(result)

# truthy and falsy values

name = ""

if name:
    print(" Name exists")
else:
    print("Empty name")

num = 4
num %= 2
if num == 0 :
    print("even")    
else:
    print("odd")

    num = 4

    if num > 0:
        print("positive.")
    elif num == 0:
     print("Zero.")
    else:
        print("negative.")

num1 = 10
num2 =20

if num1 > num2:
   print("number one is largest")
else:
   print("number two is largest")

user_name = "soma"
password = 2006

if user_name == "soma" and password == 2006:
   print("Login successfully..")
else:
   print("invald login")
#bank problem
balance = 50000
withdrawal = 2000

if balance >= withdrawal:
      a = balance - withdrawal
      print("Withdraw successful")
      print("Balance:", a)
else:
      print("Insufficient balance")

num1 = 50
num2 = 40034
num3 = 9

if num1 > num2  or num2 > num3:
      if num1 > num2 and num1 > num3:
            print("num1 is largest")
      elif num3 > num2:
            print("num 3 is largest")
      else:
            print("num2 is largest")
else:
      print("num 3 is largest")

mark = 80
match mark:
      case 90 :
            print(" A")
      case 80:
            print("B")
      case 70:
            print("C")
