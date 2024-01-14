# # # from dstructure.Stack import Stack
# # # St = Stack(3)
# # # St.push(100)
# # # St.push(200)
# # # St.push(300)
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        self.head = None
        if value:
            self.push(value)

    def display(self):
        if self.head is None:
            print("Empty Stack")
        else:
            Node = self.head
            while Node :
                print(f" | {Node.value} |", end ="\n")
                Node = Node.next
    def push(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            # self.head.next = value
            # self.head = value
            # self.head.next = None
            node.next = self.head
            self.head = node
    # def pop(self):
    #     if self.head == None:
    #         print("Empty Stack can't popup")
    #     else:
    #         self.head = self.head.next
    #         self.head.next = None
    #         value = self.head.value
    #         del self.head
    #         return f'popped{value}'

    def pop(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            return node.value


S = Stack(5)
S.push(2)
S.push(3)
S.push(4)
S.push("A")
S.push('#')
S.pop()
S.display()
#print(S())
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class Stack:
#     def __init__(self, value=None):
#         self.head = None
#         if value:
#             self.push(value)
#
#     def display(self):
#         if self.head is None:
#             print("Empty Stack")
#         else:
#             node = self.head
#             while node:
#                 print(f"{node.value} -->", end=" ")
#                 node = node.next
#
#     def push(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node
#
#
# S = Stack(5)
# S.push(2)
# S.push(3)
# S.push(4)
# S.push("A")
# S.push("#")
# S.display()
