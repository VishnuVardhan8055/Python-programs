import array as arr

# HERE TAKING THE ARRAY VALUES BY USER , We used list comprehension method

first = arr.array('i', [int(i) for i in input().split()])
second = arr.array('i', [int(j) for j in input().split()])

# Printing the array Elements

p = [first[k] for k in range(len(first))]
q = [second[l] for l in range(len(second))]
print(p, q)

# To print the sum of Two Arrays

sum = [first[m] + second[m] for m in range(len(first)) if len(first) == len(second)]
print(sum)


print(sorted(sum))

