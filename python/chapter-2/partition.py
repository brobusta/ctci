from LinkedListNode import LinkedListNode

def partition(head, x):
    start = head
    end = head
    curr = head
    while curr is not None:
        next_node = curr.next
        if curr.data < x:
            # insert at start
            curr.next = start
            start = curr
        else:
            # insert at end
            end.next = curr
            end = curr
        curr = next_node
    end.next = None
    return start

def print_node(head):
    curr = head
    while curr is not None:
        print curr.data,
        curr = curr.next

if __name__ == '__main__':
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2, node1)
    node10 = LinkedListNode(10, node2)
    node5 = LinkedListNode(5, node10)
    node8 = LinkedListNode(8, node5)
    node5_2 = LinkedListNode(5, node8)
    node3 = LinkedListNode(3, node5_2)
    head = node3
    print "before",
    print_node(head)
    newHead = partition(head,5)
    
    print "\nafter",
    print_node(newHead)

