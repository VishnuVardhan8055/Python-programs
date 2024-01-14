Matrix = [[9, 1], [2, 3]]
print(Matrix)
#print(Matrix[1])
#print(Matrix[1][0])
for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        if i == j and i == j == 0:
            del Matrix[i][j]
            Matrix[i].insert(0, 10)
        print(Matrix[i][j])
