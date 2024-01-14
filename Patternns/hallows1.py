def Hallowtriangel(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i == j or j == 1 or i == n:
                print("*",end=' ')
            else:
                print(" ",end=" ")

        print(' ')
    
#n = int(input())
#Hallowtriangel(n)

def Hallow(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            if j == n or i == 1 or j == i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print('')
n = int(input())
Hallow(n)

        
       