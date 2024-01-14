# a = int(input())
# b = int(input())
# List1 = [int(i) for i in input().split()[:a]]
# List2 = [int(j) for j in input().split()[:b]]
# # List3 = List1 + List2
# # print(sorted(List3))
#
# i, j = 0, 0
# c = []
# while (i<len(List1) and j<len(List2)):
#     if List1[i]<List2[j]:
#         c.append(List1[i])
#         i += 1
#     else:
#         c.append(List2[j])
#         j += 1
# if (i < len(List1)):
#     c.append(List1[:i])
# if (j < len(List2)):
#     c.append(List2[:j])
#


# String = input()
# l = []
# for i in String:
#     if i.isdigit():
#         l.append(i)
# print(l)
# l.sort(reverse=True)
# if(int("".join(l))%2==0):
#     print("".join(l))
# else:
#     f = 0
#     for i in range(len(l)-1,-1,-1):
#         if(int(l[i])%2==0):
#             f=1
#             l.append(l.pop(i))
#             break
#     if f==1:
#         print("".join(l))
#     else:
#         print(-1)
#


# String = input()
# List = []
# for i in range(0,len(List)):
#     if i in List[i] != '*':
#         List.pop(i)
#         List.pop(i-1)
#         # List.append(String[i])
#
# print(String)
# print(List)
# for i in String:
#     if(i.isalpha()):
#         List.append(i)
#     else:
#         List.pop()
# print("".join(List))
#
# k=int(input())

""" Virtusa Mock Test input = M#hjiks##ihs#"""

# Str = input()
# List = []
# for i in Str:
#     if i.isalpha():
#         List.append(i)
#     else:
#         List.insert(0, i)
# print("".join(List))

""" aass a2s2 """

Str = input()
l = []
"""not work"""
# count = 1
# for i in range(0, len(Str)-1):
#     if Str[i] == Str[i+1]:
#         # l.append(Str[i])
#         # l.append(Str[i+1])
#         count = count + 1
#     else:
#         #Str[i] != Str[i+1] or Str[i+1] == '':
#         l.append(Str[i])
#         l.append(str(count))
#         count = 1
#
# print(''.join(l))

# for ele in Str:
#     if ele not in l:
#         c = Str.count(ele)
#         print(ele, end="")
#         print(c, end="")
#         l.append(ele)
#
# for i in Str:
#     if i not in l:
#         c = (Str.count(i))
#         l.append(i)
#         l.append(str(c))
# print(''.join(l))

n = int(input())
w = n//7
print(w)

