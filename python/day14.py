#Revision + Coding
#practice program
#1 two sum 
nums = [2,7,11,15]
target = []
for num in nums:
    for num1 in nums[1:]:
        if num1>0 and num >0:
         if num + num1  == 9:
          target.append(num + num1)
          print(nums.index(num)," + ",nums.index(num1)," = ",target)

#word frequency
text = "python is easy and python is powerful"
freq = {}
for texts in text.split():
   freq[texts] = freq.get(texts,0) + 1
print (freq)

#first non-repeated character
w1 = "prodramming"
for w in w1:
 if w1.count(w) == 1:
  print(w)
  break
 
#find duplicate elements
number = [1,2,3,2,4,5,1]
dup_no = []
nums = []
for num in number:
 if num not in nums:
  nums.append(num)
 else:
  dup_no.append(num)
  
dup_no.sort()
print(dup_no)

#check Anagram
l1 =list(("listen")) 
l2 = list(("silent"))
l1.sort()
l2.sort()
print(l1,l2)
print(type(l1))

if l1 == l2:
 print("Anagram")
else:
 print("Not an Anagram")
   
#reverse words in a sentence
lt = ["I", "love" ,"python"]
reverse = lt[::-1]
s = " ".join(reverse)
print(s)

#most frequent element
nums = [1,1,2,3,3,3,4]
freq ={}
mfreq = ""
for num in nums:
 freq[num] = freq.get(num,0)+1
print(freq)
for key,value1 in freq.items():
 for value2 in list(freq.values())[:1]:
  if  value1 > value2:
   print(value1)

#Missing number
nums = [1,2,3,4,6,7]
for num in range(1,8):
 if num not in nums:
  print(num)
  break 

#palindrome String
text = "hi"
text1 = text[::-1].split()
if text == text1:
 print("Palindrome")
else:
 print("Not a Palindrome")

#Second largest number
nums = [10,20,30,40,50]
nums.sort(reverse=True)
print(nums[1])

#Password validater 
passw = "Python@123"
has_upper = False
has_lower = False
has_digit = False
has_special = False
special = "!@#$%^&*"

for ch in passw:

    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special:
        has_special = True

if len(passw) >= 8 and has_special and has_digit and has_lower and has_upper:
    print("Valid Password")
else:
    print("Invalid Password")

#Employee salary analysis
employee ={
    "Ram" : 25000,
    "Kumar" : 30000,
    "Priya" : 28000
}

for key,value in employee.items():
    if value in range(29000,40000):
        print("Highest Salary :",key ,"-",value)
    elif value in range(26000,29000):
        print("Average Salary:",key,"-",value)
    elif value in range(20000,26000):
        print("Lowest Salary:",key,"-",value)

#recursive sum

def recsum(n):
    if n == 0:
     return 0
    return n + recsum(n - 1)
print(recsum(5))

#recursive Factorial
def factorial(n):
   if n == 1:
    return 1
   return n * factorial(n-1)
print(factorial(5))

#inventory management
stock = {
  "Pen" : 50,
  "Book": 20,
  "Pencil": 100
}
input = str(input("Enter the product name:").title())
for name,item in stock.items():
  if name == input:
    print("Stock Available:", item)

#Bank Account system
deposit = 1000
withdraw = 300
if withdraw <= deposit:
  print("Current balance:", deposit - withdraw)

#character Frequency
input = "hello"
freq = {}
for ch in input:
  freq[ch] = freq.get(ch,0)+1
print(freq)

#Remove Duplicates While Preserving Order
input = [1,2,2,3,1,4,5]
uninum = []
for num in input:
    if num not in uninum:
        uninum.append(num)
print(uninum)

#Student Grade System
marks = [90,80,70,60,50]
max = marks[0]
min = marks[0]
total = 0
count = 0
for mark in marks:
    if mark > max:
      max.append(mark)
    if mark < min:
      min = mark
    total += mark
    count += 1
average = total / count   
print("Highest:",max)
print("Average:",average)
print("Lowest:",min)
if max in range(95 ,100):
   print("Grade: A")
elif max in range(85,95):
   print("Grade: B")
elif max in range(75,85):
   print("Grade: c")
else:
 print("Fail..")


#Mini Library System
library = {
}   
library = {"1." :"Python Basics"}
library["2."] = "Data Science"
for key,value in library.items():
   print(key , value)