n = int(input())
List = [int(i) for i in input().split()]
# Ignore the comments it's not executed
# min = 0
# max = 0
# for j in range(len(List)):
#     if List[j] < List[j+1]:
#         min = List[j]
#         n = j
# print(min)
# for k in range(j, len(List)):
#     if List[k] > List[k+1]:
#         max = List[k]
# print(max)
# Profit = max - min
# print(Profit)

#1st-method
# Da = []
# for i in range(0, len(List)-1):
#     for j in range(i, len(List)):
#         if List[i] < List[j]:
#             A = List[i] - List[j]
#             Da.append(abs(A))
# print(max(Da))
pr = 0
b = List[0]
for i in range(1, len(List)):
    if(List[i]<b):
        b = List[i]
    else:
        if(List[i]-b >pr):
            pr = List[i]-b
print(pr)



