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

def preorderTraversal(root):
    print(root.value, end = " ")
    if root.leftChild != None:
        preorderTraversal(root.leftChild)
    if root.rightChild != None:
        preorderTraversal(root.rightChild)  

def postorderTraversal(root):
    if root.leftChild != None:
        postorderTraversal(root.leftChild)
    if root.rightChild != None:
        postorderTraversal(root.rightChild)  
    print(root.value, end = " ")            

root = Node(36)
root.leftChild = Node(3)
root.rightChild = Node(12)
root.leftChild.leftChild = Node(1)
root.leftChild.rightChild = Node(3)
root.rightChild.leftChild = Node(3)
root.rightChild.rightChild = Node(4)
root.rightChild.rightChild.leftChild = Node(2)
root.rightChild.rightChild.rightChild = Node(2)

inorderTraversal(root)
print()
preorderTraversal(root)
print()
postorderTraversal(root)
