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

    def mirror(self,root):
        if root==None:
            return
        else:

            self.mirror(root.left)
            self.mirror(root.right)

            root.left,root.right = root.right,root.left


root = Node(50)
root.insert(20)
root.insert(30)
root.insert(5)
root.insert(25)
root.insert(40)
root.insert(70)
root.insert(60)
print(root.inorder(root))
root.mirror(root)
print(root.inorder(root))