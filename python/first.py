""" PrepInsta Tcs Questions """
n = int(input())
lst = [int(i) for i in input().split()[:n]]
print(lst)
for k in range(n):
    for j in range(0,k):
        if lst[j] == 0:
            lst[j] , lst[j+1] = lst[j+1] , lst[j]
    continue
print(lst)

