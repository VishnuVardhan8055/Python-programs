class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newNode = Node(data)
        if self.head:
            Cur = self.head
            while Cur.next:
                Cur = Cur.next
            Cur.next = newNode
        else:
            self.head = newNode
    def delete(self,data):
        if self.head:
            curr = self.head
            prev = None
            while curr:
                if curr.data == data:
                    curr = curr.next
                curr = curr.next
        else:
            print("Canot Delete")
    def display(self):
        curr = self.head
        while curr:
            print("|",curr.data, "|", "-->", end='')
            curr = curr.next

L = LinkedList()
L.insert("H")
L.insert(3)
L.insert(5)
L.display()
L.delete(3)
L.display()

