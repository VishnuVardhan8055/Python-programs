# lst = [int(i) for i in input().split()[:6]]
# print(lst)
# for j in range(0,len(lst)):
#      a = lst[j]
#      if a > 1:
#          b = a % 10
#          c = a
#          if b < c:
#              list.insert(b)
#          else:
#              list.insert(c)
# list=[]
# print(list)
#
# def sum_of_min_digits(numbers):
#   """
#   Returns the sum of the minimum digits from each number in the list.
#
#   Args:
#     numbers: A list of numbers.
#
#   Returns:
#     The sum of the minimum digits from each number in the list.
#   """
#
#   sum_of_min_digits = 0
#   for number in numbers:
#     min_digit = number % 10
#     while number >= 10:
#       number //= 10
#       if number % 10 < min_digit:
#         min_digit = number % 10
#     sum_of_min_digits += min_digit
#   return sum_of_min_digits
#
#
# if __name__ == "__main__":
#   numbers = [123, 456, 789]
#   print(sum_of_min_digits(numbers))
def Sum_of_Min_list(Numbers):
    Sum_Number = 0
    for Number in Numbers:
        minNumber = Number % 10
        while Number >= 10:
            Number//=10
            if Number%10 < minNumber:
                minNumber = Number%10
        Sum_Number += minNumber
    print(Sum_Number)
Numbers=[int(x) for x in input().split()[:5]]
Sum_of_Min_list(Numbers)