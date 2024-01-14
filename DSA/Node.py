class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def Print(node):
    while node is not None:
        print(node.data)
        node = node.next
head = Node(5)
head.next = Node(6)
head.next.next = Node(7)
Print(head)

