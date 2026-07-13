# #data structures
# #list
# Fruits = ["Apple","Banana","Mango"]
# print(Fruits[0])
# print(Fruits[-1])#negi
# #Slicing
# numbers= [10,20,30,40,50,60,70]
# print(numbers[1:4])

# numbers= [10,20,30,40,50,60,70]
# #append
# numbers.append(90)
# print(numbers)
# numbers.insert(1,60)
# print(numbers)
# numbers.extend([67,78,56])
# print(numbers)

# numbers.remove(50)
# print("Remove:",numbers)
# numbers.pop(1)
# print(numbers)
# del numbers[7]
# print(numbers)

# a =[1,2,3]
# print(a)
# a.clear()
# print(a)



# #sort
# a = [3,54,6,8,5,65,346,66,36,87,36]
# print("before sort:",a)
# a.sort()
# print("After sort:",a)
# a.sort(reverse = True)
# print("Desending:",a)


# #loop
# Fruits = ["Apple","Banana","Mango"]
# for i in Fruits:
#     print(i)

# a = ['apple','banana','cherry']
# for A in a:
#     print(A)
#  #nested list
# student = [
#     ["ram", 22],
#     ["sam", 20],
#     ["sri", 21]
#     ]
# print(student[0])
# print(student[1][1])

# #list comprehension
# numbers = [i for i in range(1,6)]
# print(numbers)
# #squares no
# squares = [x*x for x in range(6)]
# print(squares)

# a = [4]*4
# b = [2]*6
# print(a,b)

# #constructor
# a = list((1,2,3,"gif",4.4))
# print(a)

# b = list("bca")
# print(b)
# #remove duplicates
# #method 1
# x = [1,1,2,3,3,4,5,6,7,5,4]
# print(list(set(x)))
# #method 2
# numbers = [22,33,44,55,33,22,44,66]
# unique_no = []
# for num in numbers:
#     if num not in unique_no:
#         unique_no.append(num)
# print("unique no:",unique_no)

# #Sorting in order
# numbers = [22,33,44,55,33,22,44,66]
# for i in range(len(numbers)):
#     for j in range(i+1 ,len(numbers)):
#         if numbers[i] > numbers[j]:
#          numbers[i],numbers[j] = numbers[j],numbers[i]

# print(numbers)