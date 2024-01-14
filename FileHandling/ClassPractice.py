# sum_of_alphabetsdef sum_of_alphabets(word):
#     sum = 0
#     for i in range(len(word)):
#         sum += ord(word[i]) - 64
#     return sum
# def main():
#     word = input("Enter a Word:")
#     sum = sum_of_alphabets(word)
#     print("The sum of the alphabets of the word is:", sum)
#
# if __name__ ==  "__main__":
#     main()

# """ Ascii Values"""
# char = input("Enter the value :")
# print(f"The Ascii value of {char} is :", ord(char))

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'p', 'Q', 'R', 'W', 'X', 'Y', 'Z']
String = input("Enter the String :")
data = []
num = []
N = []

for i in range(len(String)):
    st = String[i]
    data.append(st)
for j in range(len(data)):
    if data[j] in list:
        for k in range(len(list)):
            if list[k] == data[j]:
                N = list.index(list[k])
                num.append(N)

z = 0
def Fibonacci(n):
    if n == 0:
        N.append(0)
    elif n == 1 or n == 2:
        N.append(1)
    else:
        z = Fibonacci(n-1) + Fibonacci(n-2)
        N.append(z)
def loop():
    for m in range(len(num)):
        n = num[m]
    Fibonacci(n)
loop()
print(N)


    # def fabi(n):
    #     a = 0
    #     b = 1
    #     if n <= 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     elif n > 1:
    #         for i in range(1,n):
    #             c = a + b
    #             a = b
    #             b = c
    #         N.append(c)



# print(N)
# for p in range(len(N)):
#     Q = N[p]

# def fibonacci(num):
#   total_sum = 0
#   for n in num:
#       fibonacci_sum = fibonacci(n) + fibonacci(n - 1)
#       total_sum += fibonacci_sum
#
#   return total_sum
# total_sum = fibonacci(n)
# print(total_sum)
# for l in range(len(num)):
#     it = int(num[l])
#     if it == 0 or it == 1:
#         dt = str(it)
#         dt.append(sum)
#     else:
#         d = ((it - 1) + (it - 2))
#         dt = str(d)
#         dt.append(sum)
# S = 0
# for m in range(len(sum)):
#     S = int(sum[m])
#     S += S
# print(S)
#















