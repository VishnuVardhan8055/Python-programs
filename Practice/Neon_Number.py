num = int(input())
sqr = num * num
st = str(sqr)
sum = 0
i = 0
while i < len(st):
    sum += int(st[i])
    i += 1
if num == sum:
    print("it is neon")
else:
    print("it is not neon number")



#
""" Print neon numbers upto n """
n = int(input())
for i in range(1, n+1):
    sqr = i * i
    sum = 0
    while sqr > 0:
        sum += sqr % 10
        sqr = sqr // 10
    if sum == i:
        print(i)


# n = 10000
# print("Neon numbers up to", n, "are:")
# for i in range(1, n + 1):
#     square = i * i
#     sum_of_digits = 0
#     while square > 0:
#         sum_of_digits += square % 10
#         square //= 10
#     if sum_of_digits == i:
#         print(i)
