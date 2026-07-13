# Iterators & Generators in Python
num = [10,20,30]
#Iterator
fruits = ["Apple","Banana","Orange"]
it = iter(fruits)
while True:
    try:
        print(next(it))
    except StopIteration:
        break# it = iter(num)
print(it)
#next()
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) #StopIteration exception


# Generators
def numbers():
    yield 1
    yield 2
    yield 3
n = numbers()
print(next(n))
print(next(n))
#with loop
def countdown(n):
    while n > 0 :
        yield n
        n -= 1
for i in countdown(5):
    print(i)
#Generate even numbers
def even_number(n):
    for i in range(2,n+1,2):
        yield i
for num in even_number(10):
    print(num)

# Create a generator that returns squares of numbers from 1 to n
def sqr_num(n):
    for j in range(1,n+1): 
        yield j**2
for i in sqr_num(5):
    print(i)
