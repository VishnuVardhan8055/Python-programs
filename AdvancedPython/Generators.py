""" A Generator in Python is a function that returns an iterator using the Yield keyword.
In this one, we will discuss how the generator function works in Python """

def generator():
    yield 'vishnu'
    yield 'Sanjay'
    yield 'Jai Jaganath 0 !! 0 '
genrate = generator()
# for i in genrate :
#     print(i)
print(next(genrate))

""" Return sends a specified value back to its caller whereas Yield can produce a sequence of values.
 We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.
 Yield is used in Python generators. """

# Python Program on to print the Square of the numbers b/w 1 and 10
def Genrator():
    i = 1

    while True:
        yield i * i
        i += 1
for num in Genrator():
    if num > 100:
        break
    print(num)

""" Python Generator Expression """
# In Python, generator expression is another way of writing the generator function.
# It uses the Python list comprehension technique but instead of storing the elements in a list in memory,
# it creates generator objects.

gen_expression = (i * 5 for i in range(10) if i%2 == 0)
for i in gen_expression :
    print(i)