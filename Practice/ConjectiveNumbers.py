n = int(input())
list = [int(i) for i in range(1,n+1)]
print(list)
for j in range(0,n+1):
    sum = list[j]+list[j+1]
    print(sum)