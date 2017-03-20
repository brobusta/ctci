from Stack import Stack
import sys

class StackWithMin(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.min_stack = Stack()

    def push(self, item):
        Stack.push(self, item)
        if item < self.min():
            self.min_stack.push(item)

    def pop(self):
        item = Stack.pop(self)
        if item == self.min():
            self.min_stack.pop()
        return item

    def min(self):
        if self.min_stack.isEmpty():
            return sys.maxint
        return self.min_stack.peek()

if __name__ == '__main__':
    stack = StackWithMin()
    stack.push(3)
    print stack.min()
    stack.push(4)
    print stack.min()
    stack.push(1)
    print stack.min()
    stack.pop()
    print stack.min()
    stack.pop()
    print stack.min()
