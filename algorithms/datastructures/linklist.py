class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None

    # Print List 
    def listprint(self):
        printNode = self.headNode
        while printNode is not None:
            print(printNode.dataval)
            printNode = printNode.nextNode

    # INSERTION
    # At head
    def athead(self,newData):
        NewNode = Node(newData)
        NewNode.nextNode = self.headNode
        self.headNode = NewNode
    
    # At end
    def atend(self,newData):
        NewNode = Node(newData)
        if self.headNode is None:
            self.headNode = NewNode
            return
        lastelement = self.head
        while lastelement.nextNode:
            lastelement = lastelement.nextNode
        lastelement.nextNode = NewNode

    # In between
    def inbetween(self,middle_node,newData):
        if middle_node is None:
            print('Invalid Node')
            return
        NewNode = Node(newData)
        NewNode.nextNode = middle_node.nextNode
        middle_node.nextNode = NewNode

    # Removing
    def removeNode(self,RemoveKey):
        HeadVal = self.headNode
        if (HeadVal is not None):
            if (HeadVal.dataval == RemoveKey):
                self.head = HeadVal.nextNode
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.dataval == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextNode

        if (HeadVal == None):
            return
        
        prev.nextNode = HeadVal.nextNode
        HeadVal = None

    # Reverse
    def reverse(self):
        prevNode = None
        currentNode = self.headNode
        while (currentNode is not None):
            nextNode = currentNode.nextNode
            currentNode.nextNode = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.headNode = prevNode

    # Length
    def length(self):
        count = 0
        currentNode = self.headNode
        while currentNode:
            currentNode = currentNode.nextNode
            count += 1
        print(count)
        return count

    # Middle
    def findMiddle(self,head):
        if head == None:
            return head
        slow = head
        fast = head
        while fast and fast.nextNode:
            slow = slow.nextNode
            fast = fast.nextNode.nextNode
        print("Middle "+str(slow.dataval))
        return slow

    # MergeSortHelper
    def sortedMerge(self,l,r):
        result = None

        if l == None:
            return r
        if r == None:
            return l

        if l.dataval <= r.dataval:
            result = l
            result.next = self.sortedMerge(l.next,r)
        else:
            result = r
            result.next = self.sortedMerge(l,r.next)
        return result

    # MergeSort
    def mergeSort(self,head):
        if head == None or head.nextNode == None:
            return head
        
        m = self.findMiddle(head)
        nexttomiddle = m.nextNode

        m.nextNode = None

        left = self.mergeSort(head)
        right = self.mergeSort(nexttomiddle)

        sortedlist = self.sortedMerge(left,right)
        return sortedlist

        


llist = SLinkedList()
# llist.athead("Mon")
# llist.athead("Tue")
# llist.athead("Wed")
# llist.athead("Thu")
llist.athead(15)
llist.athead(20)
llist.athead(4)
llist.athead(7)

llist.mergeSort(llist.headNode)