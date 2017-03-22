class Node(object):
    def __init__(self, data = None, adj = []):
        self.data = data
        self.adj = adj

class Graph(object):
    def __init__(self, nodes = []):
        self.nodes = nodes

class State:
    UNVISITED = 0
    VISITED = 1
    VISITING = 2

def RouteBetweenNodes(G, A, B):
    from Queue import Queue
    if A == B:
        return True
    queue = Queue()
    for u in G.nodes:
        u.state = State.UNVISITED

    A.state = State.VISITING
    queue.add(A)
    while queue.isEmpty() is False:
        node = queue.remove()
        for v in node.adj:
            if v == B:
                return True
            elif v.state == State.UNVISITED:
                v.state = State.VISITING
                queue.add(v)
        node.state = State.VISITED
    return False

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n1.adj = [n2, n3]
    n2.adj = [n1, n4]
    n3.adj = [n1, n4]
    n4.adj = [n5]
    n5.adj = [n4]
    G = Graph([n1,n2,n3,n4,n5,n6])
    print "route between n1-n5", RouteBetweenNodes(G, n1, n5)
    print "route between n1-n6", RouteBetweenNodes(G, n1, n6)
    print "route between n4-n5", RouteBetweenNodes(G, n4, n5)

