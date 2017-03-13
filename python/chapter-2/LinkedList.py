class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0
    
    def empty(self):
        return self.length == 0

    def add_first(self, data):
        oldHead = self.head
        self.head = Node(data, oldHead)
        self.length += 1

    def print_forward(self):
        curr = self.head
        while curr is not None:
            print curr.data,
            curr = curr.next

if __name__ == '__main__':
    mlist = LinkedList()
    mlist.add_first(2)
    mlist.add_first(3)
    mlist.add_first(10)
    mlist.print_forward()
