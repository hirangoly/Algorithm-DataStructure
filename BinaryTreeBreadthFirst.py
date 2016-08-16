# Binary Tree Breadth first Traversal

class Node(object):
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        
def getLevelOrder(root):
    h = height(root)
    # look why h+1 required
    for i in range(1, h+1):
        printLevel(root, i)

def printLevel(root, level):
    if root is None:
        return
    if level == 1:
        print root.data
    else:
        printLevel(root.left, level - 1)
        printLevel(root.right, level - 1)
        
def height(root):
    if root is None:
        return 0
    else:
        # calculate height of each tree
        lheight = height(root.left)
        rheight = height(root.right)
        
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
            
            
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)

# depth first level order traversal
print getLevelOrder(node)
