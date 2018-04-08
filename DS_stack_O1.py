class Stack():
    def __init__(self):
        self.stack_items = []
        self.min = []

    def push(self, item):
        if len(self.stack_items) == 0:
            self.min.append(item)
        elif item < self.min[-1]:
            self.min.append(item)

        if len(self.min) > 2:
            del self.min[0]
        self.stack_items.append(item)
        return self.stack_items

    def pop(self):
        item_pop = self.stack_items[-1]
        if item_pop in self.min and self.stack_items.index(item_pop) == len(self.stack_items) -1:
            self.min.remove(item_pop)

        print 'item popped {}'.format(item_pop)
        self.stack_items.pop(-1)
        return self.stack_items

    def findMin(self):
        if len(self.stack_items) != 0:
            min = self.stack_items[0]
            for i in self.stack_items[1:]:
                if i < min:
                    min = i
        else:
            min = None

        return min

    def findMinO1(self):
        if len(self.min) != 0:
            return self.min[-1]
        else:
            return None


# [4,5,1,3,2,5,1,3]
stack = Stack()
# []
print 'blank stack ' + str(stack.stack_items)
items = stack.push(4)
print 'items after 4 {}'.format(items)
items = stack.push(5)
print 'items after 5 {}'.format(items)
items = stack.push(1)
print 'items after 1 {}'.format(items)
items = stack.push(3)
print 'items after 3 {}'.format(items)
items = stack.push(2)
print 'items after 2 {}'.format(items)
items = stack.push(5)
print 'items after 5 {}'.format(items)
items = stack.push(1)
print 'items after 1 {}'.format(items)
items = stack.push(3)
# [4,5,1,3,2,5,1,3]
print 'items after 3 {}'.format(items)
items = stack.pop()
# 3
# [4,5,1,3,2,5,1]
print 'items after popped {}'.format(items)
min = stack.findMin()
print 'min number is {}'.format(min)
# 1
min = stack.findMinO1()
print 'min number is {}'.format(min)

# [4,5,1]
stack = Stack()
print 'blank stack ' + str(stack.stack_items)
items = stack.push(4)
print 'items after 4 {}'.format(items)
items = stack.push(5)
print 'items after 5 {}'.format(items)
items = stack.push(1)
print 'items after 1 {}'.format(items)
print 'items after 3 {}'.format(items)
items = stack.pop()
min = stack.findMin()
print 'min number is {}'.format(min)

min = stack.findMinO1()
print 'min number is {}'.format(min)

# [4]
stack = Stack()
print 'blank stack ' + str(stack.stack_items)
items = stack.push(4)
print 'items after 4 {}'.format(items)
items = stack.pop()
print 'items after popped {}'.format(items)
min = stack.findMin()
print 'min number is {}'.format(min)
min = stack.findMinO1()
print 'min number is {}'.format(min)


# [4,5,1,1]
stack = Stack()
print 'blank stack ' + str(stack.stack_items)
items = stack.push(4)
print 'items after 4 {}'.format(items)
items = stack.push(5)
print 'items after 5 {}'.format(items)
items = stack.push(1)
print 'items after 1 {}'.format(items)
items = stack.push(1)
print 'items after 1 {}'.format(items)
items = stack.pop()
min = stack.findMin()
print 'min number is {}'.format(min)

min = stack.findMinO1()
print 'min number is {}'.format(min)