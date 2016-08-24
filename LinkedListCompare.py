class Node(object):
	def __init__(self, value = None, next = None):
		self.data = value
		self.next = next
		
class LinkedList(object):
	def __init__(self):
		self.current_node = None
		
	def create(self, data):
		node = Node()
		node.data = data
		node.next = self.current_node
		self.current_node = node
		
	def size(self):
		node = self.current_node
		i = 0
		while node != None:
			i += 1
			node = node.next
		print i
		
def compareList(list1, list2):
	list1 = list1.current_node
	list2 = list2.current_node
	while list1 or list2:
		# 0 list1 is same as list2
		if list1 and list2:
			if list1.data > list2.data:
				return 1
			elif list2.data > list1.data:
				return -1
		
		# 1 if list1 size greater than list2
		if list2 and not list1:
			return 1

		# -1 if list2 size is greater than list1
		if list1 and not list2:
			return -1
			
		list1 = list1.next
		list2 = list2.next
	return 0

			
ls1 = LinkedList()
ls1.create('a')
ls1.create('b')
ls1.create('c')
ls1.create('d')
ls1.size()

ls2 = LinkedList()
ls2.create('a')
ls2.create('b')
ls2.create('c')
ls2.create('d')

ls3 = LinkedList()
ls3.create('a')
ls3.create('b')
ls3.create('c')

ls4 = LinkedList()
ls4.create('a')
ls4.create('b')
ls4.create('c')
ls4.create('d')
ls4.create('e')

ls5 = LinkedList()
ls5.create('a')
ls5.create('b')
ls5.create('c')
ls5.create('e')

# ls1 and ls2 are similar = 0
print 'ls1 and ls2 is same: ', compareList(ls1, ls2)

# ls1 is greater than ls3 = 1
print 'ls1 is greater than ls3: ', compareList(ls1, ls3)

# ls4 is greater than ls1 = -1
print 'ls4 is greater than ls1: ', compareList(ls1, ls4)

# ls5 is greater than ls1 = -1
print 'ls5 is greater than ls1: ', compareList(ls1, ls5)
