def insertionsort(lst):
    for i in range(1,len(lst)):
        temp = lst[i]
        j = i-1
        while j >= 0 and lst[j]>temp:
            if lst[j] > temp:
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = temp
    return lst
lst = [4,3,5,1,2]
print(*insertionsort(lst))
