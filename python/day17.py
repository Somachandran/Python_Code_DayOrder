# #File Handling in Python
# #Writing to a File
# file = open("student.txt","w")
# file.write("John\n")
# file.write("David\n")
# file.write("Alice\n")
# file.write("Sriram\n")
# file.close()

# #Appending to a File
# file = open("student.txt","a")
# file.write("Soma")
# file.write("\nJuinth")
# file.close()

# with open("student.txt","r") as file:
#     data = file.read()
#     print(data)

# #Reading from a File
# file = open("student.txt","r")
# data = file.read()
# print(data)
# file.close()
# #readline()
# file = open("student.txt","r")
# print(file.readline())
# print(file.readline())
# file.close()

# #readlines()
# file = open("student.txt","r")
# data = file.readlines()
# print(data)
# file.close()


# #Writing in a CSV
# import csv
# with open("student.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Age","City"])
#     writer.writerow(["Sriram",21,"Annur"])
#     writer.writerow(["Soma",20,"Gobi"])
#     writer.writerow(["Juinth",21,"Gobi"])

# #CSV Files
# import csv
# with open("student.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# #JSON Files
# #Writing JSON File
# import json
# student = {
#     "name":"soma",
#     "age":20,
#     "city":"gobi"
# }
# with open("student.json","w") as file:
#     json.dump(student,file)

# #Reading JSON file
# import json
# with open("student.json","r") as file:
#     data = json.load(file)
# print(data)
# #Access values
# print(data["name"])

# #Notes Management
# import json
# input1 = str(input("Enter the title of the note:"))
# input2 = str(input("Enter the title of the note:"))
# with open("notes.json","w") as file:
#         notes = {
#                   "title" : input1,
#                   "content" : input2
#             }              
#         data = json.dump(notes,file)      
# with open("notes.json","r") as file:
#     data = json.load(file)
# print(data)
# if data["title"] == input1:
#       print("note added successfully...")