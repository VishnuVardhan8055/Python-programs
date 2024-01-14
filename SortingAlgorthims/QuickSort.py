def partition(lst, start, end):
    p_index, pivot = start, lst[start]
    while start < end:
        while start < len(lst) and lst[start]<=pivot:
            start = start + 1
        while end > 0 and lst[end]>pivot:
            end = end - 1
        if start < end:
            lst[start], lst[end] = lst[end], lst[start]
    lst[p_index], lst[end] = lst[end], lst[p_index]
    return end
def quickSort(lst, start, end):
    if start < end:
        partitionIdx = partition(lst, start, end)
        quickSort(lst, start, partitionIdx-1) # left part
        quickSort(lst, partitionIdx+1, end)   # right part
    return lst

lst = [5,2,4,1,0]
print(*quickSort(lst, 0, len(lst)-1))
