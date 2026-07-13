# #Regular Expressions (Regex)
# #re.search()
# import re
# text = "Python is Easy"
# result = re.search("Python",text)
# if result:
#     print("Match found")
# else:
#     ("No match")

# #re.match
# import re
# text = "Python is easy"
# result = re.match("Python",text)
# if result:
#     print("Matched")

# #re.findall
# import re
# text = "cat bat rat"
# result = re.findall("at",text)
# print(result)

# #re.finditer()
# import re 
# text = "cat bat rat"
# for match in re.finditer("at",text):
#     print(match)

# #Find Digits
# import re
# text = "My age is 20"
# print(re.findall(r"\d",text))

# #Find Words
# import re 
# text = "Python123 Java456"
# print(re.findall(r"\w+",text))

# #Replacing text
# #re.sub()
# import re
# text = "I like Java"
# new_text = re.sub("Java","Python",text)
# print(new_text)

# #Validate Email
# import re
# email = "user@gmail.com"
# pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
# if re.match(pattern,email):
#     print("Valid Email")
# else:
#     print("Invalid Email")

#Validate a phone number (10 digits)
import re
ph_no = "1234567890"
pattern = r"^\d{10,}$"
if re.match(pattern,ph_no):
    print("Valid Number.")
else:
    print("Print Invalid")

#Validate a password
import re
passw = "Abcd!123"
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
if re.findall(pattern,passw):
    print("Valid Password.")
else:
    print("Invalid Password")