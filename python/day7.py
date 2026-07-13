num = 153
original = num
sum = 0

while num >0:
    digit = num % 10
    sum = sum +digit ** 3
    num=num //10

if sum == original:
    print("Armstong number")
else:
    print("Not Armstong number")

#fibonacci series
a = 0
b = 1
for i in range(10):
    print(a)
    c = a+b
    a = b
    b = c
    
#reverse number
num = 1234
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(reverse) 

#pattern
for i in range(1,7):
    print("*"*i)