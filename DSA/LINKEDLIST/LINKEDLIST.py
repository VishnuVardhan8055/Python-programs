class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        NewNode = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = NewNode
        else:
            self.head = NewNode
    def display(self):
        curr = self.head
        while curr:
            print("|", curr.data, "|", "--->", end='')
            curr = curr.next
    def delete(self,data):
        if self.head.data == data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == data:
                break
            n.next = n.next.next
            #n = n.next


L = LinkedList()
L.insert(3)
L.insert(4)
L.insert(5)
L.delete(4)
L.display()
