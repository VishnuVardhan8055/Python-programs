""" Array implementing using the module array """
import array as arr
a = arr.array('i', [1, 2, 3, 4, 3, 2, 2, 2])
print("The new created array is :", end=" ")
# a.insert(1,4)
# a.append(5)
# a.remove(3)
# a.pop()
count = a.count(2)
a.reverse()
a.extend([7, 8, 9, 0])
for i in range(0, int(len(a))):
    print(a[i], end='  ')
#print(a[0])
print(f"\n Element given count is {count}")
print(*a)
#print(f"\n Array to print reverse is {rever}")