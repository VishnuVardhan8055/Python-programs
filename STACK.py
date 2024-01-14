# def S():
#     Stack = []
#     while True:
#         inputs = input()
#         if inputs == '\n':
#             break
#         Stack.append(inputs)
#     return Stack
#
# def pop():
#     if len(Stack) == None :
#         print(" Stack Is Empyt ")
#     elif len(Stack) >= 0:
#         j = 0
#         while j >= 0:
#             Stack[j] == None
#         j += 1
# def display():
#     k = 0
#     while len(Stack) != None :
#         print('|', Stack[k],'|',end='\n')
#     k += 1
# S()
# display()
# class Stack:
#   def __init__(self):
#     self.items = []
#
#   def push(self, item):
#     self.items.append(item)
#
#   def pop(self):
#     return self.items.pop()
#
#   def display(self):
#     print(self.items)
#
#
# def take_inputs():
#   """Takes inputs from the user until the enter key is pressed.
#
#   Returns:
#     A list of the inputs.
#   """
# inputs = []
# while True:
#     input_str = input("Enter a number: ")
#     if input_str == "\n":
#       break
#     inputs.append(input_str)
# print(inputs)


# def main():
#   stack = Stack()
#   inputs = take_inputs()
#
#   for item in inputs:
#     stack.push(item)
#
#   print("The stack is:")
#   stack.display()
#
#   print("Popping the top element:")
#   print(stack.pop())
#
#   print("The stack is now:")
#   stack.display()
#
#
# if __name__ == "__main__":
#   main()

def repeat_input():
  """Repeats the input process again and again.

  The user can exit the loop by entering the word "exit".
  """
  while True:
    input_str = input("Enter a string: ")
    if input_str == "exit":
      break
    print("You entered:", input_str)


if __name__ == "__main__":
  repeat_input()


