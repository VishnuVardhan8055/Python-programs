class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self,value):
        new_Node = Node(value)
        new_Node.next = self.head
        self.head = new_Node

    def pop(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            #current = self.head
            self.head = self.head.next
    def display(self):
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
S = Stack()
S.push(1)
S.push(2)
S.display()




