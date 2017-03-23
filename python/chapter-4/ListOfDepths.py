class TreeNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return self.__str__()

def ListOfDepths(root):
    lists = []
    createListOfDepths(root, lists, 0)
    return lists

def createListOfDepths(root, lists, level):
    if root is None:
        return
    lvlist = None
    if len(lists) == level:
        lvlist = []
        lists.append(lvlist)
    else:
        lvlist = lists[level]
    lvlist.append(root)
    createListOfDepths(root.left, lists, level + 1)
    createListOfDepths(root.right, lists, level + 1)

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2, n1)
    n3 = TreeNode(3, n2)
    n6 = TreeNode(6)
    n8 = TreeNode(8)
    n7 = TreeNode(7, n6, n8)
    n5 = TreeNode(5, n3, n7)

    ret = ListOfDepths(n5)
    print ret
