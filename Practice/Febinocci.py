def febi(n):
    a, b, c = 0, 1, 0
    i = 0
    list = []
    while i < n:
        c = a + b
        a = b
        b = c
        list.append(c)
        i += 1
    print(list)
    lis =[]
    for j in range(0, len(list)):
        if j == 0 or j % 2 == 0:
            lis.append(list[j])
    x = sum(lis)
    print(x)

n = int(input())
febi(n)
