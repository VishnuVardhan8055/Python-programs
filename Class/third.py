# String = input()
# Dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
# num = int(input())
# for i in range(0, len(String)):
#     DA = String[i]
#     j = Dic.get(DA)
#     value = j - num
#     for key in Dic:
#         if Dic.get(key) == value:
#             print(key, end='')


# num = int(input())
# for i in String:
#     value = ord(i)
#     print(chr(value-num), end='')

# String = input()
# num = int(input())
# k = ""
# for i in String:
#     val = ord(i)
#     if val < 97:
#         k = k + (chr((val-num)+26))
#     else:
#         value = ord(i)
#         print(chr(value-num), end='')
# print(k)

""" Second question"""
# count = 1
# Max = 0
# n = int(input())
# List = [int(i) for i in input().split()[:n]]
# for i in range(0, len(List)-1):
#     if List[i] == (List[i+1]) - 1:
#         count = count + 1
#     else:
#         if Max < count:
#             Max = count
#             count = 1
#
# print(Max)

""" Third question """
# N = int(input())
# items = [int(i) for i in input().split()[:N]]
# K = int(input())
# sum = 0
# count = 0
# Data = sorted(items)
# for i in range(0, len(Data)):
#     if Data[i] < K:
#         if sum <= K:
#             sum = sum + Data[i]
#             count += 1
# print(count-1)

# N = int(input())
# items = [int(i) for i in input().split()[:N]]
# K = int(input())
# count = 0
# items.sort()
# for i in items:
#     if i <= K:
#         count += 1
#         K = K - i
#     else:
#         break
# print(count)

# a = int(input())
# List = []
# for k in range(a):
#     i = list(map(int, input().split()))
#     List.append(i)
# print(List)


# String = ''
# Data = None
# List = []
# for i in String:
#     if i != ' ':
#        Data = Data + i
#        d = len(Data)
#        List.insert(d, Data)
#     elif i == ' ':
#         Data = None
# print(List)

# Data = ''
# String = input()
# for i in String:
#     print(i)
# print(Data)

# Dic = {3:"hey", 4:"guys", 5:"whats", 2:"up"}
# a = input().split()
# d = {}
# for i in a:
#     d[len(i)] = i
# l = sorted(d)
# for i in l:
#     print(d[i], end = ' ')


"""5 th problem"""
a = input().split()
a.sort(key=len)
print(a)

"""6th problem"""
def fun(x):
    return x[2]
a = [[4,5,8],[9,1,0],[3,2,2],[4,7,3]]
a.sort(key=fun)  # a.sort(key=fun,reverse=True) if u give reverse = True it gives descending order or else ascending
print(a)


