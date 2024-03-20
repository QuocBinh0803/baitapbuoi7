class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def rong(self):
        return self.linkedList.head is None

    def push(self, gia_tri):
        node = Node(gia_tri)
        node.next = self.linkedList.head
        self.linkedList.head = node

    def pop(self):
        if self.rong():
            return "nguyen quoc binh"
        else:
            gia_tri_nut = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return gia_tri_nut

    def xem_dinh(self):
        if self.rong():
            return "nguyen quoc binh"
        else:
            return self.linkedList.head.value

    def xoa(self):
        self.linkedList.head = None
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.xem_dinh())  
print(stack.pop())       
print(stack.xem_dinh())  
