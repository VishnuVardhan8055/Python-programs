row = int(input())
col = int(input())
matrix = [ ]
for row in range(col):
    matrix.append([int(a) for a  in input().split()])
print(*matrix,sep='\n')
count = 0
rectangle = 0
for rows in matrix:
  for cols in rows:
    if matrix[rows,cols] == 1:
      count += 1
  if count >= 3:
    rectangle +=1
print(rectangle)
# Rows , Cols = 0 , 0
# for rows in matrix:
#   Rows += 1
# for cols in matrix:
#   Cols += 1
# print(Rows , 'X' , Cols)