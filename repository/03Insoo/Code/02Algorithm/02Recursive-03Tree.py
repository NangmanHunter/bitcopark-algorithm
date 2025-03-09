class Node:
 def __int__(self, value):
  self.left=None
  self.right=None
  self.value=value

def inorder_traversal(node):
 if node:
  inorder_traversal(node.left)
  print(node.value, end='')
  inorder_traversal(node.right)

root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(3)
root.left.right=Node(7)
root.left.left=Node(12)
root.left.right=Node(17)

inorder_traversal(root)
