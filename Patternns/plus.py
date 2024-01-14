def plus(n):
    for row in range(1,n+1):
        for col in range(1,n):
            print(" ",end=" ")
        for col in range(1,n-(n//2)):
            print("*",end=" ")
        print(' ')
    for row in range(1,(n//2)+1):
        for col in range(1,n+(n//2)):
            print("*",end=" ")
        for col in range(1,n//2+(n//2)+1):
            print("*",end=' ')
        print(" ")
    for row in range(1,n+1):
        for col  in range(1,n):
            print(" ",end=" ")
        for col in range(1,n-(n//2)):
            print("*",end=' ')
        print(' ')

n = int(input())
plus(n)