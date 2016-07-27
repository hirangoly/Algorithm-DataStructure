#Queue Implementation of arrays/List - FIFO

class Queue:
	def __init__(self):
		self.items = []

	def size(self):
		return len(self.items)
		
   	def list(self):
		return self.items

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		#self.items.insert(0, item)
		self.items.append(item)

	def dequeue(self):
		# pop take out last element - FIFO
		#self.items.pop()
		del self.items[0]
		
	def rear(self):
	    return self.items[-1]
	
	def front(self):
	    return self.items[0]
		

def main():
	q = Queue()
	
	print 'check if queue is Empty - should return True'
	print q.isEmpty()
	
	print 'initially list is empty'
	print q.list()
	
	print 'first element added is 10'
	print q.enqueue(10)
	
	print 'second element added is 30'
	print q.enqueue(30)
	
	print 'list print with 2 elements'
	print q.list()
	
	print 'dequeue - will take out 1st element in - 10'
	print q.dequeue()

	print 'print list after dequeue'
	print q.list()
	
	print 'added hello'
	print q.enqueue('hello')

	print 'print size is 2'
	print q.size()

	print 'added 10'
	print q.enqueue(10)

	print 'size - 3'
	print q.size()
	
	print 'print list - 3 elements - 30, hello, 10'
	print q.list()
	
	print 'dequeue - first element is now 30'
	print q.dequeue()

	print 'size - 2'
	print q.size()

	print 'check if queue is Empty - should return false'
	print q.isEmpty()

	print 'final list - 2 elements - hello, 10'
	print q.list()
	
	print 'print front element - hello'
	print q.front()
	
	print 'print rear element - 10'
	print q.rear()

if __name__ == '__main__':
	main()
