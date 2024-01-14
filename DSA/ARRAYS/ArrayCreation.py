import array as arr
# In array for to add the element use array_name.append("data") , For to remove the element we use array_name.remove("data")
first = arr.array('i', [1, 2, 3])
first.append(4)
first.remove(1)
#for i in range(len(first)):
#    print(first[i])
i = 0
while i < len(first):
    print(f'|{first[i]}|', end=" ")
    i += 1
print('\n')
print("ARRAY IMPLEMENT TO PRINT  USER INPUT ")
second = arr.array('i', [int(i) for i in input().split()])
print(len(second))
for i in range(len(second)):
    print(f"|{second[i]}|", end=" ")


