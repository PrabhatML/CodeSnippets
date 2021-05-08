class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None

    def printLList(self):
        node = self.headNode
        while node:
            print(node.data)
            node = node.nextNode

    def push(self,data):
        node = Node(data)
        node.nextNode = self.headNode
        self.headNode = node

    def detectloop(self):
        s = set()
        node = self.headNode

        while node:
            if node in s:
                return True
            s.add(node)
            node = node.nextNode
        return False

slist = SLinkedList()
slist.push(20)
slist.push(4)
slist.push(5)
slist.push(11)
slist.push(90)
# slist.headNode.nextNode.nextNode.nextNode = slist.headNode
if slist.detectloop():
    print("yes")
else:
    print("no")