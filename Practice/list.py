lst = []
data = [int(x) for x in input().split()[:10]]
print(data)
result =[]
#for i in range(len(data) -1, -1, -1):
i = len(data)-1
while i >= 0:
    result.append(data[i])
    i -= 1
print(result)
#print(data)


