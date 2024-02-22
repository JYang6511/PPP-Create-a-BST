"""
Part 1: Create a BSTNode class

** Reference: Linked List Class **
class Node:
   def __init__(self,data=None):
      self.data = data
      self.next = None




This class will look very similar to the Node class we wrote for our linked list, 
but should fulfill the following requirements:

The constructor should accept up to three arguments: data, left, and right
If any of the arguments are not specified, they should default to None.
Don't forget to include the self argument.
Write two magic methods (__str__() and __repr__() ) to allow the nodes to be printed. 

These two magic methods should return strings that represent the node. 
They should both return the same thing, the value of the node's data as a string.
Refer back to the magic methods activity if you need help remembering how to create magic methods for classes.
To test that these work, a node with the value 3 for its data should output 3 when printed.
Use the following code to test whether your BSTNode is functioning correctly.

node1 = BSTNode(3)
print(node1) #3

node2 = BSTNode(4, left=node1)
print(node2) #4

node3 = BSTNode()
print(node3) #None
node3.data = 5
print(node3) #5
"""

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


node1 = BSTNode(3)
print(node1) #3

node2 = BSTNode(4, left=node1)
print(node2) #4

node3 = BSTNode()
print(node3) #None
node3.data = 5
print(node3) #5

"""
Part 2: Create a BST class
"""
class BST:
  def __init__(self, root=None):
    self.root = root
    self.contents = []
  
  def __str__(self):
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output
  
  def __repr__(self):
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output
  
  def print_tree(self, node, level=0):
    if node != None:
      self.print_tree(node.right, level + 1)
      self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
      self.print_tree(node.left, level + 1)



"""
Part 3: Add functionality to your BST class
"""
def add(self,node):
  #data wrong type
  if type(node) != int and type(node) != BSTNode:
    raise ValueError("You must pass an int or a BSTNode")

"""
If the tree is empty (root points to None), put the new node at the top of the tree.
    If the tree is not empty, start at the root. 
    Compare the new node's value to the current node's value. 
        If the new node is bigger, move to the right. 
        If the new node's value is smaller, move to the left. 
        When there is no node at the current position, put the new node there.
"""