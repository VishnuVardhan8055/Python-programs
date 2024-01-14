class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class Linked_List:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None :
            print(" Linked List is Empty ('--0_0--') ")
        else :
            n = self.head
            while n is not None:
                print("|" , n.data ,"|" , "--->" , end = ' ')
                n = n.next

    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = Node(data)
        
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(data,None)
            n.next = newNode

    def add_begin(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = Node(data)
        else:
            newNode.next = self.head
            self.head = newNode

    def add_end(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(data,None)
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node is not preset")
        else:
            newNode = Node(data)
            newNode.next = n.next
            n.next = newNode

    """def add_before(self,data,x):
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n is None:
            print("Node is Empty")
        else:
            newNode = Node(data)
            newNode.next = n
            n = newNode 
            #n.next = newNode """
    def add_before(self,data,x):
        n = self.head
        while n is not None:
            if  x == n.next.data:
                break
            n=n.next
        if n.next is None:
            print("Node is Not Present in Linked List")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node        
        






LL = Linked_List()
#LL.insert(7)
#LL.insert(9)
#LL.add_begin(8)
LL.add_end(5)
LL.add_after(7,5)
LL.add_before(8,5)
LL.display()

