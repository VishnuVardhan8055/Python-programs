def star(n):
    for row in range(1,n+1):
        for col in range(row,n+1):
            if col == n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print(' ')
n = int(input())
star(n)