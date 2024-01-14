A = [[1, 2, 3], [3, 2, 1], [1, 2, 3]]
B = [[3, 2, 1], [1, 2, 3]]
Sum = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
if len(A) == len(B) or len(A[1]) == len(B[0]):
    print("Yes")
    for i in range(len(A)):
        for j in range(len(A[0])):
                Sum = A[i][j] + B[i][j]

    # for i in range(len(A)):
    #     for j in range(A[i]):
    #         for k in range(A[i]):
    #             Sum[i][j][k] = A[i][j][k] + B[i][j][k]
    # print(Sum)
