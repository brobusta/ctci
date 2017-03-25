import sys

class TreeNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

def CheckBalanced(root):
    height, balanced = CalHeight(root)
    print "height =",height
    return balanced

def CalHeight(root):
    if root is None:
        return -1, True
    hLeft, leftBalanced = CalHeight(root.left)
    if not leftBalanced:
        return (-sys.maxint-1), False
    hRight, rightBalanced = CalHeight(root.right)
    if not rightBalanced:
        return (-sys.maxint-1), False
    h = max(hLeft, hRight) + 1
    if abs(hLeft - hRight) > 1:
        return (-sys.maxint-1), False
    return h, True

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2, n1)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n2, n4)
    n6 = TreeNode(6)
    n8 = TreeNode(8)
    n7 = TreeNode(7, n6, n8)
    n5 = TreeNode(5, n3, n7)
    print CheckBalanced(n5)

