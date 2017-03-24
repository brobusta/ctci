class TreeNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return self.__str__()

def ListOfDepths2(root):
    lists = []
    current_level = []
    if root is not None:
        current_level.append(root)

    while len(current_level) != 0:
        lists.append(current_level)
        next_level = []
        for node in current_level:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        current_level = next_level
    return lists

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2, n1)
    n3 = TreeNode(3, n2)
    n6 = TreeNode(6)
    n8 = TreeNode(8)
    n7 = TreeNode(7, n6, n8)
    n5 = TreeNode(5, n3, n7)
    ret = ListOfDepths2(n5)
    print ret
