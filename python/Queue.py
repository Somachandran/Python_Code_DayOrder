# #Queue
# #Queue in Python Using List
# queue = []
# #Enqueue
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# #Remove
# queue.pop(0)
# print(queue)

# #Queue in collections.deque
# from collections import deque
# q = deque()
# #Enqueue
# q.append(10)
# q.append(20)
# q.append(30)
# print("Queue:",q)
# #Front
# print("Front:",q[0])
# #Rear
# print("Rear:",q[-1])
# #Dequeue
# removed = q.popleft()
# print("Removed:",removed)

# print("Queue:",q)
# print("Size:",len(q))

# #Using queue.Queue
# from queue import Queue
# q = Queue(maxsize=3)
# print("Size:",q.qsize())
# q.put('a')
# q.put('b')
# q.put('c')
# print("Is Full:",q.full())
# print(q.get())
# print(q.get())
# print(q.get())
# print("Is empty:",q.empty())
# q.put(1)
# print("Is empty:",q.empty())
# print("Is full:",q.full())

# #task
# from collections import deque
# q = deque()

# while True:
#     print("1.Enqueue \n 2.Dequeue\n 3.Peek\n 4.Display\n 5.Size\n 6.Exit\n")
#     i = int(input("Enter your choose 1 to 6:"))

#     if i==1:
#         val = input("Enter the Value to store:")
#         q.append(val)
#     elif i==2:
#         if not q:
#             print("Queue is Empty.")
#         else:
#             print("Dequeue value:",q.popleft())
#     elif i==3:
#         if len(q)==0:
#             print("Queue is Empty.")
#         else:
#             print("Peek is:",q[0])
#     elif i==4:
#         if len(q)==0:
#             print("Queue is Empty.")
#         else:
#             print("Queue:",list(q))
#     elif i==5:
#         print("Size is:",len(q))
#     elif i==6:
#         print("Exits")
#         break
#     else:
#         print("Invalid Option...")
#     input("\nPress Enter to continue...")
