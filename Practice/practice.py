# # # # # # #numbers = [1,2,3,4,5]
# # # # # # N = int(input())
# # # # # # lst =[int(x) for x in input().split()[:N]]
# # # # # # a = len(lst)
# # # # # # print(a)
# # # # # # #result = list(map(lambda x : 'Even' if x%2 == 0 else 'Odd',number))
# # # # # # #print(result)
# # # # # # #result = lst.index()
# # # # # # z = int(input())
# # # # # # #for i in lst:#range(len(number)) :
# # # # # # if z in lst:
# # # # # #      print(z)
# # # # # #      for i in range(len(lst)):
# # # # # #         print(lst.index(z))
# # # # # #         break
# # # # # # else:# i != z and i == len(lst):
# # # # # #     print("No element found")
# # # # # #
# # # # # text = input()
# # # # # for i in range(0,len(text)):
# # # # #     print(ord(text[i])-64)
# # # # """ To print the number of a String"""
# # # # def alphabet_position(text):
# # # #     for i in range(0,len(text)):
# # # #         if text[i] == " " or text[i] == '.' or text[i] == "'":
# # # #             continue
# # # #         print(ord(text[i])-64,end=" ")
# # # # text = input()
# # # # alphabet_position(text)
# # #
# # # text = input()
# # # for i in range(0,len(text)):
# # #     if text[i] in ('a', 'i', 'e', 'o', 'u', 'A', 'E', 'I', 'O', 'U', "'", '.', ',', '!', '?'):
# # #         continue
# # #     print(text[i], end="")
# # #
# # # def disemvowel(str):
# # #     for i in range(0,len(st)):
# # #         if st[i] in ('a', 'e', 'i', 'o', 'u', 'A', 'E','I', 'O', 'U'):
# # #             continue
# # #         print(st[i],end="")
# # # string1 = "This website is for losers LOL!"
# # # string2 = "No offense but,\nYour writing is among the worst I've ever read"
# # # st = string1
# # # disemvowel(st)
# # # st = string2
# # # disemvowel(st)
# # start = input()
# # end = input()
# # for i in range(ord(start)-1, ord(end)+1):
# #     print(chr(i), end="")
# # """ same for the above code"""
# # num = int(input())
# # a, c = 0, 0
# # b =1
# # i = 0
# # while i < num:
# #     c = a + b
# #     a = b
# #     b = c
# #     print(c)
# #     i += 1
# # list1 = [int(i) for i in input().split()]
# # list2 = [int(j) for j in input().split()]
# # List = list1 + list2
# # print(sorted(List))
class Solution:
    def isValid(self, s: str) :
        list = ["[]", "()", "{}"]
        if len(s) == 1:
            if s in list:
                print("true")
            else:
                print("false")
        elif len(s) < 1:
            print("true")
s = input()
Sol = Solution()
Sol.isValid(s)


