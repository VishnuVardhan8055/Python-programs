# word = "abcaabdbc"
#
# re = set(word)
# for i in re:
#     print(i, word.count(i))
# print(word.count())
#
from collections import Counter
s = input()
t = input()
count_s = Counter(s)
count_t = Counter(t)
# Calculate the absolute difference between counts and sum them
total_steps = sum((count_s - count_t).values())
print(total_steps)
print(sorted(Counter(s).values()))
print(sorted(set(Counter(t).values())))
print(Counter(s).keys())
