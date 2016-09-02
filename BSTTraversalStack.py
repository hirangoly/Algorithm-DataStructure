# Binary tree traversal without recursion using stack
class Node(object):
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        
def InorderTraversal(root):
    currentNode = root
    st = []
    done = 0
    
    while not done:
        if currentNode is not None:
            st.append(currentNode)
            currentNode = currentNode.left
            
        else:
            # backtrack 
            if len(st) > 0:
                currentNode = st.pop()
                print currentNode.data
                
                # right
                currentNode = currentNode.right
            else:
                done = 1
                
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

InorderTraversal(root)
