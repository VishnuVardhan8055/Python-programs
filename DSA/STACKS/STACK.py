class Node:
    def __init__(self, data):
        self.head = None
        self.data = data
class Stack:
    def __init__(self, data):
        self.head = None
        if data:
            self.push(data)
    def display(self):
        if self.head == None:
            print("Stack is UnderFlow")
        else:
            #node = self.head
            while self.head:
                print(f"|{self.head.data}|", end="\n")
                self.head = self.head.next
    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def pop(self, pop):
        if self.head == None:
            print("Stack is Under Flow")
        else:
            self.head = self.head.next
            self.head.next = self.head.next.next

S = Stack('')
S.push(1)
S.push(3)
S.push(5)
S.push(7)
S.display()




