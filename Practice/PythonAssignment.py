# N = int(input())
# list = [int(i) for i in input().split()[:N]]
# print(list)
# # Lenght_Stick = len(list)
# # print(Lenght_Stick)
# # Cut the list into 3 & 4
# Stick1 = []
# Stick2 = []
# Stick3 = []
# Stick4 = []
# for j in range(0,len(list)):
#     if j < 3:
#         Stick1.append(list[j])
#     elif j >= 3:
#         Stick2.append(list[j])
# for k in range(len(Stick1)):
#     if k < 1:
#         Stick3.append(list[k])
#     elif k <= 2:
#         Stick4.append(list[k])
# print(len(Stick1))
# print(len(Stick2))
# Total_cost = len(list) + len(Stick1) + len(Stick2) + len(Stick4)
# print(Total_cost)

n = int(input())
list = [None]*n
# print(len(list))
cut1 = int(input())
cut2 = int(input())
Stick1 = []
Stick2 = []
i = 0
for i in range(len(list)):
    if i < 3:
        Stick1.append(list[i])
    elif i >= 3:
        Stick2.append(list[i])

Stick3 =[]
Stick5 =[]
for j in range(len(Stick1)):
    if j < 1 :
        Stick3.append(Stick1[j])
    elif j >= 1:
        Stick5.append(Stick1[j])
# print(len(Stick1))
# print(len(Stick2))
# print(len(Stick5))
Total_Cost = len(list) + len(Stick1) + len(Stick2) + len(Stick5)
print(Total_Cost)