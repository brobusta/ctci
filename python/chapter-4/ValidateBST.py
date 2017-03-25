import sys

class TreeNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

def ValidateBST(root):
    return isBST(root, -sys.maxint-1, sys.maxint)

def isBST(node, minValue, maxValue):
    if node is None:
        return True
    if node.data > minValue and node.data <= maxValue:
        leftIsBST = isBST(node.left, minValue, node.data)
        if not leftIsBST:
            return False
        rightIsBST = isBST(node.right, node.data, maxValue)
        if not rightIsBST:
            return False
        return True
    return False

if __name__ == '__main__':
    n1 = TreeNode(2)
    n2 = TreeNode(2, n1)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n2, n4)
    n6 = TreeNode(6)
    n8 = TreeNode(8)
    n7 = TreeNode(7, n6, n8)
    n5 = TreeNode(5, n3, n7)
    print ValidateBST(n5) 
