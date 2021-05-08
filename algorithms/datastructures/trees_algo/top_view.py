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


    def topview(self,root):
        if root is None:
            return
        m = defaultdict(list)
        q = []
        hd = 0

        root.hd = hd
        q.append(root)  

        while q:
            temp = q.pop(0)
            hd = temp.hd
            if hd not in m:
                m[hd] = temp.data

            if temp.left:
                temp.left.hd = hd - 1
                q.append(temp.left)
            if temp.right:
                temp.right.hd = hd + 1
                q.append(temp.right)
        # i = 0
        # temp = root
        # while temp:
        #     m[i] = temp.data
        #     i -= 1
        #     temp = temp.left

        # temp = root
        # i = 0
        # while temp:
        #     m[i] = temp.data
        #     i += 1
        #     temp = temp.right

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
(root.topview(root))                