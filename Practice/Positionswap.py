lst = [int(i) for i in input().split()[:6]]
print(lst)
print(lst[1])
print("To the Change the Two position , \n Give the position numbers to change :")
p1 = int(input('position1 :'))
p2 = int(input('position2 :'))
lst[p1-1] ,lst[p2-1] = lst[p2-1] ,lst[p1-1]
print(lst)
