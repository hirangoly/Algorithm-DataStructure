# Linked list implementation
class Node():
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList():
	def __init__(self):
		self.current_node = None

	def addNode(self, data):
		new_node = Node()
		new_node.data = data
		new_node.next = self.current_node
		self.current_node = new_node
		return new_node
	
	def printList(self):
		node = self.current_node
		while node != None:
			print(node.data)
			node = node.next
			
	def deleteNode(self, data):
		node = self.current_node
		prev_node = None
		found = False
		while node != None and found is False:
			if node.data == data:
				found = True
				prev_node.next = node.next
				node = prev_node
			else:
				prev_node = node
				node = prev_node.next
				
	def search(self, data):
		node = self.current_node
		while node != None:
			if node.data == data:
				return node.data, node
			else:
				node = node.next

ls = LinkedList()
ls.addNode(2)
ls.addNode(6)
ls.addNode(10)

ls.printList()

ls.deleteNode(6)

ls.printList()

print(ls.search(2))