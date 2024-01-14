class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def Print(self):
        #if self.value is None:
           # print("No Root Presents")
        #if self.value is not None:
            #print(self.value)
        if self.left:
            self.left.Print()
        print(self.value)
        if self.right:
            self.right.Print()

    def Find(self,value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.Find(value)
        elif value>self.value:
            if self.right is None:
                return False
            else:
                return self.right.Find(value)
        else:
            return True
    def MimMum(self):
        if self.left:
            return self.left.MimMum()
        return self.value

    def MaxMum(self):
        if self.right:
            return self.right.MaxMum()
        return self.value
tree = TreeNode(10)
#tree.insert(1)
#tree.insert(3)
#tree.insert(56)
#tree.insert(45)
#tree.Print()
#print(TreeNode)
lst = [1,3,56,45,40,30,100]
#for i in range(1,len(lst)):
i = 0
while i < len(lst):
    tree.insert(lst[i])
    i += 1
tree.Print()

print(tree.Find(56))
#tree.Print()
print(tree.MimMum())
print(tree.MaxMum())

