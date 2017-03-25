class TreeNode(object):
    def __init__(self, data = None, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
    def __str__(self):
        return str(self.data)

def Successor(node):
    if node is None:
        return None
    if node.right is not None:
        return findLeftMost(node.right)
    else:
        q = node
        x = node.parent
        while x is not None and x.left != q:
            q = x
            x = x.parent
        return x
    
def findLeftMost(node):
    if node.left is None:
        return node
    else:
        return findLeftMost(node.left)

if __name__ == '__main__':
    n1 = TreeNode(2)
    n2 = TreeNode(2, n1)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n2, n4)
    n6 = TreeNode(6)
    n8 = TreeNode(8)
    n7 = TreeNode(7, n6, n8)
    n5 = TreeNode(5, n3, n7)
    n1.parent = n2
    n2.parent = n3
    n3.parent = n5
    n4.parent = n3
    n7.parent = n5
    n6.parent = n7
    n8.parent = n7
    print "successor of n1 = " + str(Successor(n1))
    print "successor of n2 = " + str(Successor(n2))
    print "successor of n3 = " + str(Successor(n3))
    print "successor of n4 = " + str(Successor(n4))
    print "successor of n5 = " + str(Successor(n5))
    print "successor of n6 = " + str(Successor(n6))
    print "successor of n7 = " + str(Successor(n7))
    print "successor of n8 = " + str(Successor(n8))
 
