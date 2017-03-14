class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

def List_Add(List, data):
    oldHead = List.head
    List.head = Node(data, oldHead)

def List_Print(List):
    curr = List.head
    while curr is not None:
        print curr.data,
        curr = curr.next

if __name__ == '__main__':
    mList = LinkedList()
    List_Add(mList, 1)
    List_Add(mList, 2)
    List_Add(mList, 9)
    List_Print(mList)
