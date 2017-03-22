class TreeNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def createMinimalBST(A):
    N = len(A)
    if N == 0:
        return None
    mid = N / 2
    root = TreeNode(A[mid])
    root.left = createMinimalBST(A[:mid])
    root.right = createMinimalBST(A[mid+1:])
    return root

def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print root.data,
        printInOrder(root.right)

if __name__ == '__main__':
    root = createMinimalBST([1,3,5,7,9,12,14,15,17,19])
    printInOrder(root)
