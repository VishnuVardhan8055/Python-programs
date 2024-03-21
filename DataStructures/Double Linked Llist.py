# Double Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Double_LL:
    def __init__(self):
        self.head = None
    def printLL(self,data):
        if self.head is None:
            print("Linked List is empty !")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.ref
    def printLL_reverse(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "--->", end="")
                n = n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not Empty")
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self,data,x):
        if self.head is None:
            print("LL is Empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present is DLL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("LL is Empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present is DLL")
            else :
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node
               # else:
                 #   self.head = new_node
                #n.pref = new_node


Dll = Double_LL()
Dll.insert_empty(23)
Dll.insert_empty(13)
Dll.printLL(10)