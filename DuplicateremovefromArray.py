# # list = ([int(i) for i in input().split()])
# # for i in range(0,len(list)):
# #     for j in range(1,len(list)):
# #         if list[j] == list[i]:
# #             pass
# #     list.remove(list[i])
# # print(list)
# list = ([int(i) for i in input().split()])
# for i in range(0,len(list)):
#     for j in range(1,len(list)):
#         if list[j] == list[i]:
#             pass
#     list.remove(list[i])
# print(list)

list = [1, 5, 5, 3, 4]
reverse = []
for i in range(0, len(list)):
    if list[i] not in reverse:
        reverse.append(list[i])
print(reverse)

