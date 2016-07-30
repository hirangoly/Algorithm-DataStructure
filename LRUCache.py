# LRU chache - capacity, cache = {key:data}, LRU = {key,time}
# get(key) - if key is in cache, then need to get data, increase tm with 1, and refresh data (push item to start of list) else return -1. 
# set (key, data) - If key is not in cache insert data in cache to start of list. If cache is full remove 1 item that key has min tm from list and then insert item to the start. Also, if key is old
# reference - https://www.kunxi.org/blog/2014/05/lru-cache-in-python/

class LRUCache(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.cache = {}
		self.lru = {}
		self.tm = 0
		
	def get(self, key):
		if key in self.cache:
			# return data for requested key
			self.lru[key] += 1
			return self.cache[key], self.lru[key]
		return -1
		
	def set(self, key, data):
		if self.capacity <= len(self.cache):
			# remove 1 item from dict that has min tm
			old_key = min(self.lru, key = self.lru.get)
			del self.cache[old_key]
			del self.lru[old_key]
			
		if key not in self.cache:
			# insert new key in cache
			self.cache[key] = data
			self.lru[key] = self.tm
		else:
			# refresh data
			self.cache[key] = data
			self.lru[key] = self.tm + 1
			
		print 'return complete cache and lru dict'
		print self.cache, self.lru
			
		# return data of new key and time
		return self.cache[key], self.lru[key]
			
def main():
	lrc = LRUCache(capacity=3)
	
	# first check if there is any element
	print 'check if any element - no element'
	print lrc.get('name')
	
	# insert first data
	print '1st data inserted - rangoli'
	print lrc.set('name', 'Rangoli')
	
	# check cache - Rangoli, 1
	print 'get first element, and time'
	print lrc.get('name')
	
	# again get element - Rangoli, 2
	print 'get first element, and time'
	print lrc.get('name')
	
	# insert second data
	print '2nd data inserted - MTV'
	print lrc.set('address', 'MTV')
	
	# insert third data
	print '3rd data inserted - SW'
	print lrc.set('stream', 'SW')
	
	# insert third data
	print '4th data inserted - LV'
	print lrc.set('visit', 'LV')
	
	
	

if __name__ == '__main__':
	main()