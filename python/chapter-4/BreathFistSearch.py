class State:
    UNVISITED = 0
    VISITED = 1
    VISITING = 2

class Node(object):
    def __init__(self, data = None, adj = []):
        self.data = data
        self.adj = adj
        self.state = State.UNVISITED
    def __str__(self):
        return str(self.data)

def BreathFistSearch(root):
    if root is None:
        return
    from Queue import Queue
    queue = Queue()
    root.state = State.VISITING
    queue.add(root)
    while queue.isEmpty() is False:
        node = queue.remove()
        for child in node.adj:
            if child.state is State.UNVISITED:
                child.state = State.VISITING
                queue.add(child)
        visit(node)
        node.state = State.VISITED
 
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
    BreathFistSearch(n0) 
