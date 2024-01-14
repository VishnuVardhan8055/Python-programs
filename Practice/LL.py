class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked is Empty('0' __ '0')")
        current = self.head
        while current :
            print('|',current.data,'|',"-->",end=" ")
            current =  current.next 


    def insert(self,data):
        newNode = Node(data)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
                
    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:    
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode  
    def pop(self,data):
        if self.head is None:
            print("Linked List is Empty we can't pop the linked list")
        
        else:
            current = self.head
            #while current :
                #current = current.next
            current = None
            #current.next = current



L1 = LinkedList()
#L1.insert(77)
#L1.insert(5)
#L1.insert(34)
L1.insert(45)
L1.insert(27)
L1.insert(1)
L1.insert(29)
#L1.push(1)
#L1.push()
L1.pop(1)
L1.display()





    