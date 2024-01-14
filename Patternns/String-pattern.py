def String(n):
    a = len(n)
    for i in range(1,a+1):
        for j in range(i,a):
            print(" ",end=" ")
        for j in range(0,i):
            print(n[j],end=" ")
        print()
    b = len(n)
    for i in range(1,b+1):
        for j in range(i,b):
            print(n[j],end=" ")
        print()
n = input()
String(n)