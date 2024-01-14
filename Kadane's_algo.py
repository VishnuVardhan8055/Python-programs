#List = [-1, 3, 4, 1, 0, -9]
def Kadanes(List):
    Max = List[0]
    curr = 0
    for i in range(0, len(List)):
        curr = curr + List[i]
        if (Max <= curr):
            Max = curr
        if (curr < 0):
            curr = 0
    return(curr)
List = [-1, 3, 4, 1,0, -9]
Kadanes(List)





