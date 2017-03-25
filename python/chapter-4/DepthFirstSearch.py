class Node(object):
    def __init__(self, data = None, adj = []):
        self.data = data
        self.adj = adj
        self.visited = False
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return self.__str__()

class Graph(object):
    def __init__(self, nodes = []):
        self.nodes = nodes

def DepthFirstSearch(root):
    if root is None:
        return
    visit(root)
    root.visited = True
    for node in root.adj:
        if node.visited is not True:
            DepthFirstSearch(node)

def visit(node):
    print node,

if __name__ == '__main__':
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n0.adj = [n1, n4, n5]
    n1.adj = [n3]
    n2.adj = [n1]
    n3.adj = [n2, n4]
    DepthFirstSearch(n0)
