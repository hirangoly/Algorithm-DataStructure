# enqueue - add a item in queue
# dequeue - remove first item from queue
# list - list of items in queue
# size - number of items in queue

class queue(object):
	def __init__(self):
		self.items = []
		
	def enqueue(self, name):
		self.items.insert(0,name)
		
	def dequeue(self):
		self.items.pop()
		
	def qsize(self):
		return len(self.items)
		
	def qlist(self):
		return self.items
		
		
q = queue()

q.enqueue('rangoly')
q.enqueue('ashish')
q.enqueue('arham')

# size of queue
sz = q.qsize()
print(sz)
print(q.qlist())

q.dequeue()

#size of queue
print(q.qsize())

# list of queue after dequeue 1 item
print(q.qlist())