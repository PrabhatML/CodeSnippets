from collections import defaultdict
class Node:

    def __init__(self,key):
        self.data = key
        self.left = self.right = None

    
    def vertical_order_traversal(self,root):
        if root is None:
            return
        queue = []
        m= defaultdict(list)
        hd = 0

        root.hd = 0
        queue.append(root)

        while queue:
            temp = queue.pop(0)
            hd = temp.hd
            print(temp.data,hd)
            m[hd].append(temp.data)

            if temp.left:
                temp.left.hd = hd - 1
                queue.append(temp.left)

            if temp.right:
                temp.right.hd = hd + 1
                queue.append(temp.right)
    
        return m
    
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

root = Node(50)
root.insert(40)
root.insert(70)
root.insert(30)
root.insert(45)
root.insert(60)
root.insert(75)
print(root.inorder(root))

print(root.vertical_order_traversal(root))