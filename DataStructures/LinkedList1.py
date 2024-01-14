class Node :
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            #n = self.head
            while  self.head is not None: # // while n is not None:
                print(self.head.data , "--->" , end = "")      # // print(n.next)
                self.head = self.head.next   
                #n=n.next


    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    """def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node = self.head
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(data,None)
                
                """
    def add_end(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            while(n.next):
                n = n.next
            n.next = Node(data,None)

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n=n.next
        if n is None:
            print("Node is not present in Linked List")
        else:
            #LL1.add_begin(data)
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

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
            
    def  delete_begin(self,data=None):
        if self.head is None:
            print("Node is empty")
        else:
            self.head = self.head.next


    def delete_end(self,data=None):
        if self.head is None:
            print(" LL is empty so we cant delete ")
        else:
            n=self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def delete_by_value(self,x):
        if self.head is None:
            print("cant delete LL is empty")
            return
        if x == self.head.data :
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x == n.next.data:
                break
            n=n.next
        if n.next is None:
            print("None is not present")
        else:
            n.next = n.next.next


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(390)
LL1.add_end(40)
LL1.add_end(50)
LL1.add_begin(70)
#LL1.print()
LL1.add_after(11,20)
LL1.add_before(27,50)
LL1.delete_begin()
LL1.delete_end()
LL1.delete_by_value(10)
LL1.print()
"""

class Node:
    def __init__(self,data,ref=None):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    #def insert_at_end(self,data):
     #   if self.head is None:
    def print(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref


LL = LinkedList()
LL.insert_at_begin(7)
LL.insert_at_begin(8)
LL.print()
"""