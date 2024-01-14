import array as arr
Array = arr.array('i', [int(i) for i in input().split()])
Arr = [Array[j] for j in range(len(Array))]
print(Arr)
#print("Reversed Array")
l = len(Array)-1
while l >= 0:
    print(f'|{Array[l]}|', end="")
    l -= 1
print("\n")
print(list(reversed(Arr)))
print(sorted(Arr))
