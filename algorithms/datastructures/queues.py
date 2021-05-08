# Queue
class Queue:
    def __init__(self):
        self.queue = list()
    def addtoq(self,val):
        if val not in self.queue:
            self.queue.insert(0,val)
            return True
        else:
            return False
    def removefromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return "No element"
TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.removefromq())
print(TheQueue.removefromq())