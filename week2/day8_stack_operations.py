class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items)==0

s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())     #3
print(s.pop())    #3
print(s.peek())    #2
