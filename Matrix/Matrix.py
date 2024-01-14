a = int(input())
b = int(input())
# i, j = 0, 0
# Matrix = []
# for i in range(1, a+1):
#     row = []
#     for j in range(1, b+1):
#         elements = int(input("Enter the row :{}, col :{} ".format(i, j)))
#         row.append(elements)
#     Matrix.append(row)
# print(Matrix)

Matrix = [[int(input("Enter the Row{}, col{} :".format(i, j)))for i in range(a)]for j in range(b)]
print(Matrix)
