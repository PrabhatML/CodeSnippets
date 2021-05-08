# Trees
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def insert(self,data):
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Inorder -> Left -> Root -> Right
    def inorderTransversal(self,root):
        res = []
        if root:
            res = self.inorderTransversal(root.left)
            res.append(root.data)
            res = res + self.inorderTransversal(root.right)
        return res

    # Preorder -> Root -> Left -> Right
    def preorderTransversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTransversal(root.left)
            res = res + self.preorderTransversal(root.right)
        return res

    # Postorder -> Left -> Right -> Root
    def postorderTransversal(self,root):
        res = []
        if root:
            res = self.postorderTransversal(root.left)
            res = res + self.postorderTransversal(root.right)
            res.append(root.data)
        return res

    # Search
    def findval(self,val):
        if val < self.data:
            if self.left is None:
                return "Not Found"
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return "Not Found"
            return self.right.findval(val)
        else:
            return "Found"

    def minValueNode(self,node):
        current = node
        while (current.left is not None):
            current = current.left
        return current

    def deleteNode(self,root,key):
        if root is None :
            return root

        if key < root.data:
            root.left = self.deleteNode(root.left,key)
        elif key > root.data:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            # temp = self.minValueNode(root.right)
            # root.data = temp.data
            # root.right = self.deleteNode(root.right,temp.data)
            
            succParent = root
            succ = root.right

            while succ.left != None:
                succParent = succ
                succ = succ.left

            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
            
            root.data = succ.data

        return root
root = Node(50)
root.insert(30)
root.insert(20)
root.insert(40)
root.insert(70)
root.insert(60)
root.insert(80)
root.printTree() 
print(root.inorderTransversal(root))
root.deleteNode(root,50)
print(root.inorderTransversal(root))