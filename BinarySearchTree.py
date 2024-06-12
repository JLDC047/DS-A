class Node():
    def __init__(self,data):
        self.value = data
        self.leftChild = None
        self.rightChild = None    

def inorderTraversal(root):
    if root.leftChild != None:
        inorderTraversal(root.leftChild)
    print(root.value, end = " ")
    if root.rightChild != None:
        inorderTraversal(root.rightChild)  

def insert(root,item):
    if root != None:
        print (root.value)
    if root == None:
        return Node(item)
    elif root.value > item: 
        print("left")
        root.leftChild = insert(root.leftChild, item)
    elif root.value < item:
        print("right")
        root.rightChild = insert(root.rightChild, item)
    return root       

def search(root, item):
    if item == root.value:
        return root
    elif root.value > item and root.leftChild != None:
        return search(root.leftChild, item)
    elif root.value < item and root.rightChild != None:
        return search(root.rightChild, item)   
    else: 
        return -1

root = Node(8)
root.leftChild = Node(3)
root.rightChild = Node(10)
root.leftChild.leftChild = Node(1)
root.leftChild.rightChild = Node(6)
root.rightChild.rightChild = Node(14)
root.rightChild.rightChild.leftChild = Node(13)
root.leftChild.rightChild.leftChild = Node(4)
root.leftChild.rightChild.rightChild = Node(7)

inorderTraversal(root)

"""root = None
for i in range(0,9):
    root = insert(root, int(input("Value: ")))   

inorderTraversal(root)""" 

print(search(root, 12))
