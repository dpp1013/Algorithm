class BTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BTree(newNode)
        else:
            t = BTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BTree(newNode)
        else:
            t = BTree(newNode)
            t.right = self.right
            self.right = t

    def getRight(self):
        return self.right

    def getLetf(self):
        return self.left

    def setRoot(self, value):
        self.key = value

    def getRoot(self):
        return self.key
