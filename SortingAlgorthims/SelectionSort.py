def SelectionSort(lst):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] < lst[j]:
                lst[i] ,lst[j]  = lst[j], lst[i]
    return lst

lst = [5,3,4,2,1]
print(SelectionSort(lst))
