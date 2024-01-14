Number = int(input())
# last_digit = Number % 10
# Remaining_Number = Number // 10
# print(last_digit)
# print(Remaining_Number)
# Reverse_Number = (last_digit*10)+Remaining_Number
# print(Reverse_Number)
temp = Number
Reverse = 0
while Number > 0:
    Rev = Number%10
    Reverse = (Reverse*10)+Rev
    Number = Number // 10
print("Reverse Number is = ", Reverse)

