list = [1,4,5,6,7,8]
x = int(input())
y = int(input())
for i in range(0,len(list)):
    if list[i] == x :
        a = i
for j in range(0,len(list)):
    if list[j] == y:
        b = j
print(list[a+1:b])