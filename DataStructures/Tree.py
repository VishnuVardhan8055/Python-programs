class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
    def insert(self, data):
        #newnode = Node(data)
        if self.data is None :
            self.data = Node(data)
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    def display(self,r):
        if r is None:
            return
        else:
            display(r.left)
            print(r.data)
            display(r.right)

T = Node(9)
T.insert(5)
T.insert(10)
T.insert(11)
T.insert(6)
T.insert(1)
T.insert(0)
display(T)



