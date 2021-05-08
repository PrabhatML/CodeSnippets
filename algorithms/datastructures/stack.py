# Stack
class Stack:
    def __init__(self):
        self.stack = []
    def add(self,val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
    def remove(self):
        if len(self.stack) <= 0:
            return "Empty stack"
        else:
            return self.stack.pop()
AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
print(AStack.remove())