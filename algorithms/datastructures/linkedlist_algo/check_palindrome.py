class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
    
class SlinkedList:
    def __init__(self):
        self.headNode = None

    def printLList(self):
        node = self.headNode
        while node is not None:
            print(node.data)
            node = node.nextNode

    def insert_head(self,data):
        newNode = Node(data)
        newNode.nextNode = self.headNode
        self.headNode = newNode
        
    def ispalindrome(self):
        i = self.headNode
        ispal = True
        stack = []
        while i:
            stack.append(i.data)
            i = i.nextNode
        
        i = self.headNode
        while i:
            stack_ele = stack.pop()
            if i.data == stack_ele:
                pass
            else:
                ispal = False
                break
            i = i.nextNode
        return ispal

llist = SlinkedList()
llist.insert_head("s")
llist.insert_head("a")
llist.insert_head("s")
llist.printLList()
print(llist.ispalindrome())