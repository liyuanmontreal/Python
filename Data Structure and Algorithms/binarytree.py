
# Python program to introduce Binary Tree
  
# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    # A function to do inorder tree traversal
    def printInorder(root):
  
        if root:
    
            # First recur on left child
            printInorder(root.left)
    
            # then print the data of node
            print(root.val),
    
            # now recur on right child
            printInorder(root.right)
    
    # A function to do postorder tree traversal
    def printPostorder(root):
    
        if root:
    
            # First recur on left child
            printPostorder(root.left)
    
            # the recur on right child
            printPostorder(root.right)
    
            # now print the data of node
            print(root.val),
    
  
    # A function to do preorder tree traversal
    def printPreorder(root):
    
        if root:
    
            # First print the data of node
            print(root.val),
    
            # Then recur on left child
            printPreorder(root.left)
    
            # Finally recur on right child
            printPreorder(root.right)  

    # Iterative Method to print the
    # height of a binary tree
    def printLevelOrder(root):
    
        # Base Case
        if root is None:
            return
        
        # Create an empty queue
        # for level order traversal
        queue = []
    
        # Enqueue Root and initialize height
        queue.append(root)
    
        while(len(queue) > 0):
        
            # Print front of queue and
            # remove it from queue
            print (queue[0].data)
            node = queue.pop(0)
    
            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)
    
            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

# create root
root = Node(1)
''' following is the tree after above statement
     1
    / \
  None None'''
  
root.left     = Node(2)
root.right     = Node(3)
  
''' 2 and 3 become left and right children of 1
        1
        / \
        2     3
    / \ / \
None None None None'''
  
  
root.left.left = Node(4)
'''4 becomes left child of 2
        1
    /     \
    2         3
    / \     / \
4 None None None
/ \
None None'''


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)
#12453
  
print("\nInorder traversal of binary tree is")
printInorder(root)
#42513
  
print("\nPostorder traversal of binary tree is")
printPostorder(root)
#45231

print ("Level Order Traversal of binary tree is -")
printLevelOrder(root)
#12345