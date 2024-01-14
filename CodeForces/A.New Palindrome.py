num = int(input())
list = []
for i in range(0, num):
    a = input()
    list.append(a)
for j in range(0, num):
    data = list[j]
    rev = data[::-1]
    if data == rev:
        if len(data) == 2 or len(data) == 3 or len(data) == 5:
            print("NO")
        else:
            print("YES")
