#LIFO
class stack(object):
	def __init__(self):
		self.items = []
		
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		self.items.pop()
		
	def size(self):
		return len(self.items)
		
	def list(self):
		return self.items
		
s = stack()

s.push('rangoly')
s.push('r')
s.push('Ashish')
s.push(4)

# list of total items
print(s.size())
print(s.list())

# remove an item
s.pop()

# list after removing 1 item
print(s.size())
print(s.list())