# DoubleLinkedList
class Node:
    def __init__(self,data):    
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.headNode = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.headNode
        if self.headNode is not None:
            self.headNode.prev = new_node
        self.head = new_node

    def insertAfter(self,prev_node,data):
        if prev_node is None:
            return "Issue"
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev =prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def append(self,data):
        new_node = Node(data)
        if self.headNode is None:
            self.headNode = new_node
            return
        laste = self.headNode
        while laste.next:
            laste = laste.next
        laste.next = new_node
        new_node.prev = laste
        return
        
    def printList(self,node):
        while node:
            print(node.data)
            last = node
            node = node.next
        while last:
            print(last.data)
            last = last.prev

llist = DoublyLinkedList()
# Insert 6. So the list becomes 6->None
llist.append(6)
# Insert 7 at the beginning.
# So linked list becomes 7->6->None
llist.push(7)
# Insert 1 at the beginning.
# So linked list becomes 1->7->6->None
llist.push(1)
# Insert 4 at the end.
# So linked list becomes 1->7->6->4->None
llist.append(4)
# Insert 8, after 7.
# So linked list becomes 1->7->8->6->4->None
llist.insertAfter(llist.head.next, 8)
llist.printList(llist.head)