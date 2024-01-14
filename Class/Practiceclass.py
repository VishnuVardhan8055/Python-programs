String = input()
List = []
l = []
Data = ['@', '$', "#", "!"]
for i in range(len(String)):
    if String[i] not in Data:
        List.append(String[i])
print(List)

# for i in String:
#     if(i.isalpha()):
#         l.append(i)
# l.reverse()
# for i in range(len(String)):
#     if (not String[i].isalpha()):
#         l.insert(i, String[i])
# print("".join(l))
