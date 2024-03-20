class Stack:
    def __init__(self):
        self.list = [] 
    def __str__(self):
        values = self.list[::-1] 
        values = [str(x) for x in values]
        return '\n'.join(values)  
    def isEmpty(self):
        return len(self.list) == 0  
    
    def push(self, value):
        self.list.append(value)   
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()   
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[-1]
    def delete(self):
        self.list = []
stack = Stack()
print(stack.isEmpty())  
stack.push(1)
stack.push(2)
stack.push(3)

print(stack)  

print(stack.peek())  
print(stack.pop())   
print(stack)         

stack.delete()
print(stack.isEmpty())  