# #dictionary
# student = {
#     "id" : 101,
#     "name":"soma",
#     "department":"BCA",
#     "cgpa" : 8.5 
# }
# print(student)
# #Accessing
# print(student["name"])
# print(student.get("name"))
# print(student.get("city"))

# #adding new item
# student["dob"] = "04|02|2006"
# print(student)

# #updating
# student["cgpa"] = 8.7
# print(student["cgpa"])
# student["age"] = 20

# #removeing
# student.pop("age")#pop()
# print(student)

# del student["name"]
# print(student)

# student.clear()
# print(student)

# student = {
#     "id" : 101,
#     "name":"soma",
#     "department":"BCA",
#     "cgpa" : 8.5 
# }

# #methods
# print("Keys:",student.keys())
# print("Value:",student.values())
# print("Both keys and value:",student.items())
# print("pop o:",student.pop("cgpa"))
# print("pop item:",student.popitem())
# student2 = student.copy()
# print(student2)

# #looping
# student = {
#     "name" : "soma",
#     "age" : 20
# }
# for key in student:
#     print(key)

# #values

# for value in student.values():
#     print(value)

# #key -value
# for key,value in student.items():
#     print(key,value)

# #nested dict
# students = {
#     101:{
#         "name" : "soma",
#         "age" : 20
#                 },
#     102:{
#         "name" : "sriram",
#         "age" : 22
#     }
# }
# print(students)
# print(students[101]["name"])

# #dict in list
# student = {
#     "name" : "ram",
#     "Skills":["python","Java","SQL"]
# }

# print(student["Skills"][0])

# square = {
#     x:x*x
#     for x in range(1,6)
# }
# print(square)

# #Frequency
# word = "banana"
# freq = {}
# for ch in word:
#     freq[ch] = freq.get(ch,0) + 1

# print(freq)

# #number
# nums = [1,2,3,4,5,1,4,3,6,1,3]
# freq = {}
# for num in nums:
#     freq[num] = freq.get(num,0)+1

# print(freq)

# mark = {
#     "math" : 90,
#     "science": 95,
#     "english":99
# }
# print(max(mark.values()))

# students_DB = {
#     101:{
#         "name":"soma",
#         "age": 20
#     },
#     102:{
#         "name" : "ram",
#         "age" : 20
#     },
#     103:{
#         "name" : "sri",
#         "age" : 20
#     }

# }
# print(students_DB)