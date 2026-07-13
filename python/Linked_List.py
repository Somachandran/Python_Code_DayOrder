#Creating a Linked List
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Create nodes
first = node(10)
second = node(20)
third = node(30)
#Connect nodes
first.next = second
second.next = third

# #Traversing a Linked List
# current = first
# while current:
#     print(current.data)
#     current = current.next

class linklist:
    def __init__(self):
        self.head = None
    #Insert at Beginning
    def insert_begining(self,data):
        new_node = node(data)
        new_node.next = first
        self.head = new_node

    #Insert at End
    def insert_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
     #Delete a Node
    def delete(self,key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current  = current.next
        print(None)

    #Search in Linked List
    def search(self,value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
l1 = linklist()
l1.hard = first
l1.insert_begining(5)
l1.delete(5)
l1.insert_end(40)
print(l1.search(20))

l1.display()
