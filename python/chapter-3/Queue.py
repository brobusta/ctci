class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self, item):
        # add to last
        node = self.QueueNode(item)
        if self.last is not None:
            self.last.next = node
        self.last = node
        if self.first is None:
            self.first = node
    
    def remove(self):
        if self.first is None:
            raise ValueError("Queue underflow")
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last == None
        return data

    def peek(self):
        if self.first is None:
            raise ValueError("Queue underflow")
        return self.first.data

    def isEmpty(self):
        return self.first is None

    class QueueNode(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node

if __name__ == '__main__':
    queue = Queue()
    queue.add(4)
    queue.add(5)
    queue.add(6)

    print queue.peek()
    print queue.isEmpty()
    e1 = queue.remove()
    print e1
    e2 = queue.remove()
    print e2
    e3 = queue.remove()
    print e3
    print queue.isEmpty()

