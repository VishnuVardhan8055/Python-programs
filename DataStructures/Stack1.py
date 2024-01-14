"""1. Stack Operation by using List """
Stack = []
Stack.append(1)
Stack.append(2)
Stack.append(3)
Stack.append(4)
print(Stack)
Stack.pop()
print(Stack)
Stack.pop()
print(Stack)

""" 2. Stack Implement using deque """
from collections import deque
stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
stack.pop()
print(stack)

""" 3. Stack Implement using LifoQueue """
from queue import LifoQueue
stack = LifoQueue(maxsize = 3)
print(stack.qsize)
stack.put('a')
stack.put('b')
stack.put('c')
print(stack)
print(stack.full())
print("Elements popped from the stack ")
print(stack.get())
print(stack.get())
print(stack.empty())








