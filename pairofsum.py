def pairSum(arr, s):
    # Write your code here.
    lst = [int(x) for x in input().split()[:arr]]
    for i in range(0,len(lst)//2):
        for j in range(0,len(lst)):
            if lst[i]+lst[j] == s:
                print(lst[i], lst[j])
arr, s = map(int, input().split())
#s = int(input())
pairSum(arr, s)
