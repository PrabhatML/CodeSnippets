class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

    def inorder(self,root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res += self.inorder(root.right)
        return res
    
    # def height(self,root):
    #     if root is None:
    #         return 0
    #     else:
    #         lheight = self.height(self.left)
    #         rheight = self.height(self.right)

    #         if lheight > rheight:
    #             return lheight+1
    #         else:
    #             return rheight+1

    # def printlevelorder(self,root):
    #     h = self.height(root)
    #     for i in range(1,h+1):
    #         self.printGivenLevel(root,i)

    # def printGivenLevel(self,root,level):
    #     if root is None:
    #         return
    #     if level == 1:
    #         print(root.data,end=" ")
    #     elif level > 1:
    #         self.printGivenLevel(root.left,level-1)
    #         self.printGivenLevel(root.right,level-1)
    def printLevelOrder(self,root):
        if root is None:
            return
        queue = []
        queue.append(root)

        while(len(queue)>0):
            print(queue[0].data)
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

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


root = Node(50)
root.insert(10)
root.insert(90)
root.insert(20)
root.insert(60)
root.insert(50)
root.insert(5)
root.insert(10)
print(root.inorder(root))
print(root.printLevelOrder(root))