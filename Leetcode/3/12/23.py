# S = input()
# print(list(reversed(S)))
# count = 0
# for i in range(len(S)):
#     if S[i] != " ":
#         count += 1
#     elif S[i] == " ":
#         break
# print(count)
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         count = 0
#         S = list(reversed(s))
#         for i in range(len(S)):
#             if S[i] != ' ':
#                 count += 1
#             elif S[i] == " ":
#                 if S[0] == ' ' and S[1] == ' ':
#                     continue
#                 else:
#                     break
#         return count

li = [1, 7, 9, 5]
print(sorted(li))

# nums = [1, 4, 1, 6, 2, 4]
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] == nums[j] and i != j:
#             nums[i] = " "
#             nums.append(nums[i])
# print(sorted(nums))
