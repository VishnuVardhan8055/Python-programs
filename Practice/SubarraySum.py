def Subarray_Sum(S,a):
    for i in range(1,len(a)):
        total_sum = 0
        for j in range(i,len(a)):
            total_sum += a[j]
            if total_sum == S:
                print(i, " to ", j)
            elif total_sum > S:
                total_sum -= a[i]

N , S = map(int, input().split())
a = [int(x) for x in input().split()[:N]]
Subarray_Sum(S,a)
