# # # import roman
# # # str = input()
# # # d = int(input())
# # # print(roman.fromRoman(str))
# # # print(roman.toRoman(d))
# #str = input()
daa = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'DM': 900, 'M': 1000}
data = dict(reversed(daa.items()))
print(data)
number = int(input())
roman = ''
for value in data:
    quotent = number // data[value]

    number -= quotent * data[value]

    roman += value * quotent
print(roman)
#
# romann = int(input())
# List = []
# for i in range(0, n):
#     number = input()
#     List.append(number)
# for j in range(0,len(List)):
#     Data = ['4123456789123456', '4123356789123456', '5123-4567-8912-3456']
#     if List[j] in Data:
#         print("Valid")
#     elif List[j] not in Data:
#         print("Invalid")
