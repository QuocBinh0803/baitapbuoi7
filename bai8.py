class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next_node):
        self._element = element
        self._next = next_node

class QueuesLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
queue = QueuesLinked()
print(queue.isEmpty()) 
print(len(queue))     