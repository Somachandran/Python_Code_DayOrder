#Binary Tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node("A")
root.left=Node("B")
root.right=Node("C")
root.left.left=Node("D")
root.left.right=Node("E")
#Preorder Traversal
def preorder(node):
    if node is None:
        return
    print(node.data)
    print(node.left)#.data
    print(node.right)
preorder(root)


#Binary Search Tree (BST) Insert 
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def insert(root,value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root
root = None
for i in [50,30,70,20,40,60,80]:
    root = insert(root,i)