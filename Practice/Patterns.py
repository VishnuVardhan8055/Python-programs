def reverse(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print(' ',end=" ")
        for k in range(i,n):
            print('*',end=' ')
        for l in range(i,n+1):
            print("*",end=' ')
        print()
n = 5
reverse(n)
#
def hill(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(" ",end=' ')
        for k in range(i , n+1):
            print("*", end=' ')
        for l in range(1,i):
            print(" ",end=" ")
        for m in range(i , n+1):
            print("*",end=" ")
        print()
n = int(input())
hill(n)
#
#
# def mirror(n):
#     for i  in range(1,n+1):
#         for j in range(1,i+1):
#             print(">",end=" ")
#         print()
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             print(" ",end=' ')
#         for k in range(1,i):
#             print(" ",end=" ")
#         for l in range(i,n+1):
#             print("<",end=" ")
#         print()
# #n = int(input())
# #mirror(n)
#
# def Cap(n):
#     for i in range(1,n+1):
#         for k in range(i,n+1):
#             print(" ",end=' ')
#             print()
#         #for l in range():
#
#     for j in range(1,n+1):
#         for m in range(1,j+1):
#             if m == j :
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
#
# n =int(input())
# Cap(n)
