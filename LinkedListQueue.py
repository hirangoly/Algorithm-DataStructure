# queue implementation of linked list

class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        

class LinkedListQueue(object):
    def __init__(self):
        #initialize linked list
        self.current_node = None
        
    def enqueue(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.current_node
        self.current_node = new_node
    
    def dequeue(self):
        node = self.current_node
        prev_node = None
        while node != None:
            if node.next == None:
                #this needs to delete
                prev_node.next = None
                return
            else:
                prev_node = node
                node = prev_node.next 
    
    def list(self):
        node = self.current_node
        while node != None:
            print node.data
            node = node.next
            
    def size(self):
        node = self.current_node
        size = 0
        while node != None:
            size += 1
            node = node.next
            
        print size
        
    def isEmpty(self):
        if self.current_node is None:
            return True
        else:
            return False

    def front(self):
        # retrive first element in
        node = self.current_node
        while node != None:
            if node.next == None:
                return node.data
            else:
                node = node.next

    def rear(self):
        # retrive last element in
        node = self.current_node
        return node.data
                
def main():
	q = LinkedListQueue()
	
	print 'check if queue is Empty - should return True'
	print q.isEmpty()
	
	print 'initially list is empty'
	print q.list()
	
	print 'first element added is 10'
	print q.enqueue(10)
	
	print 'second element added is 30'
	print q.enqueue(30)
	
	print 'list print with 2 elements - 30, 10'
	print q.list()
	
	print 'dequeue - will take out 1st element in'
	print q.dequeue()

	print 'print list after dequeue - 30'
	print q.list()
	
	print 'added hello'
	print q.enqueue('hello')
	
	print 'print size is 2'
	print q.size()

	print 'added 10'
	print q.enqueue(10)
	
	print 'size - 3'
	print q.size()
	
	print 'print list - 3 elements - 10, hello, 30'
	print q.list()
	
	print 'dequeue - first element is now 30'
	print q.dequeue()
	
	print 'size - 2'
	print q.size()
	
	print 'check if queue is Empty - should return false'
	print q.isEmpty()

	print 'final list - 2 elements - 10, hello'
	print q.list()
	
	print 'print front element - hello'
	print q.front()
	
	print 'print rear element - 10'
	print q.rear()

if __name__ == '__main__':
	main()

        
