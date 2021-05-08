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
    
    def zigzag(self,root):
        if root is None:
            return
        
        currentlevel = []
        nextlevel = []

        ltr = True

        currentlevel.append(root)

        while len(currentlevel) > 0:
            temp = currentlevel.pop(-1)
            print(temp.data)

            if ltr:
                if temp.left:
                    nextlevel.append(temp.left)
                if temp.right:
                    nextlevel.append(temp.right)
            else:
                if temp.right:
                    nextlevel.append(temp.right)
                if temp.left:
                    nextlevel.append(temp.left)
            
            if len(currentlevel) == 0:
                ltr = not ltr
                currentlevel,nextlevel = nextlevel,currentlevel

root = Node(50)
root.insert(20)
root.insert(30)
root.insert(5)
root.insert(25)
root.insert(40)
root.insert(70)
root.insert(60)
print(root.inorder(root))
root.zigzag(root)