def BubbleSort(lst):
    for i in range(len(lst)):
        for j in range(0,(len(lst)-1)):
            if lst[j] > lst[j+1] :
                lst[j] , lst[j+1] = lst[j+1] ,lst[j]
    return lst
        

lst = [1,3,4,2,5]
print(*BubbleSort(lst))