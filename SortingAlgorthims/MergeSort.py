def merge(lst1, lst2):
    i, j, res = 0, 0, []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    if i < len(lst1):
        res.extend(lst1[i:])
    if j < len(lst2):
        res.extend(lst2[j:])
    return res


def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    leftPart = mergeSort(lst[:mid])
    rightPart = mergeSort(lst[mid:])
    return merge(leftPart, rightPart)
lst = [2,4,1,3,0]
print(mergeSort(lst))