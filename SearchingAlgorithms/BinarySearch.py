def BinarySearch(lst,key):
    start = 0
    end = len(lst)+1
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == key:
            return True
        if key < lst[mid]:
            end = mid-1
        elif key > lst[mid]:
            start = mid+1
    return False
n = int(input())
lst = list(map(int,input().split()[:n]))
key = int(input())
print(BinarySearch(lst,key))