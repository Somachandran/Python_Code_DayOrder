#for
for i in range(5):
    print(i)

#while
i = 0
while i <= 5:
    print(i)
    i += 1
#multiple loop
for i in range(2,6):
    for j in range(3,5):
        print(i,j)

#patten
for i in range(1,6):
    print("*"*i)

for i in range(10):#break
    if i == 5:
        break
    print(i)

for i in range(5):#continue
    if i == 5:
        continue
    print(i)

for i in range(5):#pass
 pass

#tables
num = 6
for i in range(1,11,1):
    print("tables:",num*i)

#factorial 
num =5 
fact = 1
for i in range(1,num+1):
    fact = fact*i
    print(fact)

    #prime number
for num in range(2,22):
    prime = True
for i in range(2,num):
    if num % i == 0:
        prime = False
        break
    if prime:
     print(num)