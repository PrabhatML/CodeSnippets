from collections import defaultdict

class Node:
    def __init__(self,key):
        self.data = key
        self.left = self.right = None

    def inorder(self,root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res += self.inorder(root.right)
        return res

    def insert(self,data):
        if self.data:
            if data <= self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    node = Node(data)
                    self.left = node
            elif data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    node = Node(data)
                    self.right = node
        else:
            self.data = data


    def leftview(self,root):
        if root is None:
            return
        q = []
        q.append(root)  
        m = []
        while q:
            n = len(q)
            for i in range(1,n+1):
                temp = q.pop(0)

                if i==1:
                    m.append(temp.data)

                if temp.left:
                    q.append(temp.left)

                if temp.right:
                    q.append(temp.right)

        for i in (m):
            print(i)

root = Node(20)
root.insert(8)
root.insert(22)
root.insert(5)
root.insert(3)
root.insert(4)
root.insert(25)
root.insert(10)
root.insert(14)
print(root.inorder(root))
(root.leftview(root))                