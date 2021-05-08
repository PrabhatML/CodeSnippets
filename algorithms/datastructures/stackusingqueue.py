from queue import Queue

class Stack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self,data):
        self.q2.put(data)

        while self.q1:
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q1,self.q2 = self.q2,self.q1

    def pop(self):
        if self.q1.empty():
            return
        self.q1.get()