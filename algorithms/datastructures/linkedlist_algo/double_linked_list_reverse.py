class Node:
    def __init__(self,data):
        self.prev = self.next = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def printList(self,node):
        while node is not None:
            print(node.data)
            node = node.next

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev


llist = DoublyLinkedList()
# Insert 6. So the list becomes 6->None
llist.push(6)
# Insert 7 at the beginning.
# So linked list becomes 7->6->None
llist.push(7)
# Insert 1 at the beginning.
# So linked list becomes 1->7->6->None
llist.push(1)
# Insert 4 at the end.
# So linked list becomes 1->7->6->4->None
llist.push(4)
# Insert 8, after 7.
# So linked list becomes 1->7->8->6->4->None
llist.printList(llist.head)
llist.reverse()
llist.printList(llist.head)
