class TreeNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return self.__str__()

def InOrderPrint(root):
    if root is not None:
        InOrderPrint(root.left)
        print root,
        InOrderPrint(root.right)

def PreOrderPrint(root):
    if root is not None:
        print root,
        PreOrderPrint(root.left)
        PreOrderPrint(root.right)

def PostOrderPrint(root):
    if root is not None:
        PostOrderPrint(root.left)
        PostOrderPrint(root.right)
        print root,

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2, n1)
    n3 = TreeNode(3, n2)
    n6 = TreeNode(6)
    n8 = TreeNode(8)
    n7 = TreeNode(7, n6, n8)
    n5 = TreeNode(5, n3, n7)
    InOrderPrint(n5)
    print ""
    PreOrderPrint(n5)
    print ""
    PostOrderPrint(n5)
    print ""
