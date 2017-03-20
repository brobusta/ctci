class Stack(object):
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise ValueError("Stack underflow")
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item):
        node = self.StackNode(item)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.top is None:
            raise ValueError("Stack underflow")
        return self.top.data

    def isEmpty(self):
        return self.top is None

    class StackNode(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(10)
    print stack.peek()
    item = stack.pop()
    print item
    print stack.isEmpty()
    print stack.pop()
    print stack.pop()
    print stack.isEmpty()
