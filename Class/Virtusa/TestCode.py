n = int(input())
List = []
Data = []
for i in range(0, n):
    if i == 0:
        List.append('1')
    else:
        List.append('0')
z = ''.join(List)
k = str(z)
print(int(z))
for i in range(int(z), int(z)*10):
    count = 0
    for j in k:
        if j == '0':
            count = count + 1
    if count == 2 or count > 2:
        Data.append(k)
print(len(Data)+1)

