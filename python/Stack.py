# #Stack
# #Using List as Stack
# stack = []#Empty stack

# #Push Operation Use append()
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# print(stack)

# #Pop Operation
# stack.pop()
# item = stack.pop()
# print(stack)
# print(item)

# #Peek Operation
# stack = [10,20,30]
# print(stack[-1])

# #Checking Empty Stack
# stack = []
# if not stack:
#     print("Empty")
# #method2
# if len(stack)==0:
#     print("empty")

# #Size of stack
# stack = [1,2,3,4,5]
# print(len(stack))

# #Stack Class
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self,data):
#         self.stack.append(data)
    
#     def pop(self):
#         if self.is_empty():
#             return "Stack Underflow"
#         return self.stack.pop()

#     def peek(self):
#         if self.is_empty():
#             return "Stack Underflow"
#         return self.stack[-1]
    
#     def is_empty(self):
#         return len(self.stack)== 0
    
#     def size(self):
#         return len(self.stack)
    
#     def display(self):
#         print(self.stack)
# #Using the Stack Class
# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.display
# print(s.peek())
# print(s.pop())
# s.display()

# #Student Book Stack Management
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self,book_name):
#         self.stack.append(book_name)
       
#     def peek(self):
#         if self.is_empty():
#             return "Stack Underflow"
#         return self.stack[-1]
    
#     def pop(self):
#         if self.is_empty():
#             return "Stack Empty"
#         return self.stack.pop()
    
#     def size(self):
#         if self.is_empty():
#             return "IS EMPTY"
#         return len(self.stack)
    
#     def display(self):  
#         print(self.stack)

#     def is_empty(self):
#         return len(self.stack)==0


# s = Stack()
# s.push("Machine Learning")
# s.push("Algorithms")
# s.push("Data Structures")
# s.push("Python Basics")
# s.display()
# print(s.peek())
# print(s.pop())
# print(s.size())