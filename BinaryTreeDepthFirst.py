class Node(object):
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None
		

def printInOrder(root):
	if root:
		printInOrder(root.left)
		print(root.data),
		printInOrder(root.right)
		
def printPreOrder(root):
	if root:
		print(root.data),
		printPreOrder(root.left)
		printPreOrder(root.right)
		
def printPostOrder(root):
	if root:
		printPostOrder(root.left)
		printPostOrder(root.right)
		print(root.data),
		
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# print Depth search BT In Order
print 'Depth search BT In Order'
print printInOrder(root)

# print Depth search BT Pre Order
print 'Depth search BT Pre Order'
print printPreOrder(root)

# print Depth search BT Post Order
print 'Depth search BT Post Order'
print printPostOrder(root) 
