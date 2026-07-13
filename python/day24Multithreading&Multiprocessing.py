# #Multithreading & Multiprocessing
# # Multithreading
# import threading
# def task():
#     print("Task Running")
# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)

# t1.start()
# t2.start()

#Multiprocessing
from multiprocessing import Process

def task():
    print("Process Running")

if __name__ == "__main__":
    p1 =Process(target=task)
    p2= Process(target=task)

    p1.start()
    p1.join()
    p2.start()
