#string
c = """welcome
to 
python 
programmming"""
print(c)

#Indexing
text = "python"
print(text[0])
print(text[3])
print(text[-1])

#Slicing
text = "programming"
print(text[0:4])
print(text[3:7])
print(text[:5])
print(text[5:])
#immutability
s = "aBCDEF"
s = "A" + s[1:]
print(s)
#updating
s = "ABCD EF"
s1 ="H" + s[1:]
s2 = s.replace("ABC","abc")
print(s1)
print(s2)

#delete
s = "abs"
print(s)
del s
#with step
print(text[::2])
#reverse
print(text[::-1])
#concatennation
first = "hello"
last = "friend"
print(first+" "+last)
#Repetition
print("python " * 4)
#menbership o
text = "python"
print("p" in text)
print("z" not in text)
#length
text = "oops codings"
print(len(text))

#Escape characters
print("Hello\nFriend")#\n
print("python\tJava\tC++")#\t
print("He said \"Hello\"")#""

#Formatting
#1.f-string
name = "soma"
age = 20
print(f"My name is {name} and i am {age} years old")
#expressinos
a = 10
b = 20
print(f"Sum = {a+b}")
#decimal
pi = 3.141592
print(f"{pi:.2f}")
#format
s = "My name is {} and I am {} years old.".format("chandran" , 20)
print (s)
 
#comparison
s1 = "apple"
s2 = "banana"
print(s1 == s2)
print(s1 != s2)
print(s1< s2)
#loop
s = "ABCDEF"
for char in s:
    print(char)

# method
s = "Hello World"
print(s.upper())
print(s.lower())
s = "   ABC   "
print(s.strip())

s = "Python is fun "
print(s)
print(s.replace("fun","awesome"))
s = "python programming"
print(s.startswith("p"))
print(s.endswith("g"))
print(s.capitalize())
print(s.title())
print("PyThOn".swapcase())
text = "apple mango orange"
print(text.split())
print(".".join(text))
print(text.find("m"))
print(text.index("m"))#same but with error
print("Python".ljust(15))
print("Python".rjust(15))
print("Python".center(15))

#enumerate 
fruits = ["apple" ,"banana" ,"cherry"]
for index, fruits in enumerate(fruits):
    print(index,fruits)

    #practice
#reverse
text = "arun"
print(text[::-1])

#count vowels
i = "programmings"
count = 0
for i in text.lower():
    if i in "aeiou":
        count += 1
print(count)

#palindrome
text = str(input("Enter a text:"))
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

    