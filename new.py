print("Hello Mac User")
N = int(input())
lst = list(map(int, input().split()[:N]))
print(len(lst))
z = int(input())
if z in lst:
    print(z)
    for i in lst:
        result = lst.index(z)
        print("At index of :" , result)
        break
else:
    print("No element found")
