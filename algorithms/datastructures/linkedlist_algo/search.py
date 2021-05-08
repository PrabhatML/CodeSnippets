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

    def push(self,val):
        node = Node(val)
        node.nextNode = self.headNode
        self.headNode = node

    def search(self,val):
        if not val:
            return False

        node = self.headNode
        while node:
            if node.data == val:
                return True
            node = node.nextNode
        return False

llist = SLinkedList()
llist.push(4)
llist.push(5)
llist.push(6)
llist.push(41)
llist.push(24)
llist.push(49)
llist.printLList()
print(llist.search(7))