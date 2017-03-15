class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def append(head, data):
    if head is None:
        head = Node(data)
    else:
        cur = head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
    return head

def add(head, data):
    if head is None:
        head = Node(data)
    else:
        oldHead = head
        head = Node(data, oldHead)
    return head
