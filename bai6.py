class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:  # Thêm dấu hai chấm
            yield curNode  # Sử dụng yield thay vì return
            curNode = curNode.next
linked_list = LinkedList()
linked_list.head = Node(1)
linked_list.head.next = Node(2)
linked_list.head.next.next = Node(3)

for node in linked_list:
    print(node)

