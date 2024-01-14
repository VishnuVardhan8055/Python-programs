# # # List = [i for i in input()]
# # # temp = 0
# # # for j in range(0, len(List)):
# # #     n = List[j]
# # #     if int(n) % 2 == 0:
# # #         temp = temp + int(n)
# # # print(temp)
# # #
# # # # Method 2
# # # A = int(input())
# # # s = 0
# # # while(A):
# # #     if((A%10)%2==0):
# # #         s = s + (A%10)
# # #     A = A // 10
# # # print(s)
# # #
# # #___ Third Program
# # S = input()
# # Sum = 0
# # j = len(S)
# # for i in range(0, len(S)):
# #     Sum = Sum + (int(S[i]) ** j)
# # j = -1
# # print(Sum)
# #
# #
# # 4th Problem find the max number in array
#
#
# N = int(input())
# List = [i for i in input().split()[:N]]
# # Max = 0
# # for j in range(0, len(List)):
# #     if int(List[j]) > 0:
# #         if int(List[j]) > Max:
# #             Max = int(List[j])
# # print(Max)
# # DA = sorted(List)
# # print(DA)
# # print(DA[0])
# n = int(input())
# a = list(map(int, input().split()))
# max = 0
# for i in a:
#     if i > max:
#         max = i
# print(max)
# # ---> Map
# a = list(map(int, '6789')) #
# print(a)
#
#
#
#
#
# nums = [6,5,4,8]
# print(nums)
# print(sorted(nums))
# Sot = sorted(nums)
# Data = []
# for i in range(0, len(nums)):
#     for j in range(0, len(Sot)):
#         if nums[i] == Sot[j]:
#             Data.append(j)
# print(Data)


class Solution:
    def leftRightDifference(self, List):
        LeftSum = []
        RightSum = []
        DATA = []
        for i in range(len(nums)):
            if i == 0:
                LeftSum.append(0)
            else:
                LeftSum.append(sum(nums[0:i]))
        for j in range(len(nums), 0):
            if j == len(nums):
                RightSum.append(0)
            else:
                RightSum.append(sum(nums[j:0]))
        for k in range(len(LeftSum)):
            DATA.append(LeftSum[k] - RightSum[k])
        return DATA
List = [10, 4, 8, 3]
Sol = Solution()
Sol.leftRightDifference(List)
