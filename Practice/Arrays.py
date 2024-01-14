import array as arr
numbers = arr.array('i',[10,20,30])
""" 
Here arr is the object of import array  and .array is the declaring of array.
"""
print(numbers) # *---> To Print the arrays
print(len(numbers)) #  *---> To print the length of array
print(numbers[0]) # *---> to print the array value at index use to syntax must ( array_name[index_position])
print(numbers.index(10)) # *---> To Print the value placed at index to use syntax must (array_nae.index(value_in_array))

# to print the array elements by for loop
for i in numbers:
    print(i)

# by using range() and len() in for loop
for elements in range(len(numbers)) :
    print(numbers[elements])

# How to add a new value in to array
numbers.append(40) # """ append will add element to last to the sequence . """
print(numbers)
 
# How to insert a new number to array 
numbers.insert(0,50) # """ insert will add a number to array by the taking of index postion first were to insert """
print(numbers)

# extend the array
numbers.extend([60,70,80])
print(numbers)

# remove
numbers.remove(50) # *---> remove will remove the element from sequence by taking the removable element.
print(numbers) # """ If u defaltly perform remove without giving any number it will remove defaltly last element of the sequence"""

#pop()
numbers.pop(2)# *---> pop will perform to remove the data elements from sequence by index value
print(numbers)