# num = input()
# l = []
# if int(num)%2 != 0:
#     print(num)
# else:
#     for i in range(0, len(num)):
#         if int(num[i])%2 != 0:
#             l.append(num[i])
#         elif int(num[i])%2 == 0 and i == len(num):
#             print(int(i))
# if l != []:
#     print("".join(max(l)))

k = int(input())
N = int(input())
count = 0
for i in range(1, N, k):
    print(i)
    if i == 0:
        count = count+1
    elif i >= 1:
        count = count+1
print(count)


# List = [1, 2, 3, 4, 5]
#
# for i in range(0, len(List), 2):
#   print(List[i])
#
# a = int(input())
# b = int(input())
# for i in range(0,b,a):
#     print(i)
