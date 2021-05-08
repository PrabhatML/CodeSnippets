class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self,data):
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(data)

        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()

q = Queue()
q.enqueue(3)
q.enqueue(5)
q.enqueue(2)

print(q.dequeue())
        