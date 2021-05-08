from collections import defaultdict

class Node:
    def __init__(self,key):
        self.data = key
        self.left = self.right = None

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

    def inorder(self,root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res += self.inorder(root.right)
        return res

    def bottomview(self,root):
        if root is None:
            return
        
        queue = []
        m = defaultdict(list)

        queue.append(root)
        root.hd = 0


        while len(queue)!=0:
            temp = queue.pop(0)
            hd = temp.hd
            m[hd] = (temp.data)
            print(temp.data,m) 

            if temp.left:
                temp.left.hd = hd-1
                queue.append(temp.left)
            
            if temp.right:
                temp.right.hd = hd+1
                queue.append(temp.right)
        
        for i in sorted(m):
            print(i,m[i])

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
print(root.bottomview(root))