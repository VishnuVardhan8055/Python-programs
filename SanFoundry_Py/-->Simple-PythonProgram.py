""" 1. Python Program to Check Whether a Given Number is Even or Odd using Recursion """
def check(n):
    if (n > 2):
        return (n % 2 == 0)
    return (check(n-2))
n =  int(input("Enter the Number Whether it is Even or Odd :"))
if check(n) == True :
    print("Number is Even")
else:
    print("Number is Odd")


""" 2. Python Program to Check Whether a Number is Positive or Negative """
def Num(N):
    if N > 0:
        print("Number is Positive")
    else:
        print("Number is Negative")
N = int(input("Enter the number to check Positive or Negative :"))
Num(N)


""" 3. Python Program to Print All Odd Numbers in a Range """
N = int(input("Enter the Number for a range to Print the Odd Numbers: "))
i = 0
while i < N:
    if i % 2 != 0:
        print("Odd numbers up-to n given is :",i)
    i += 1


""" 4. Python Program to Check if a Number is a Palindrome """
N = input("Enter a Number for Palindrome to check :")
Reverse = N[::-1]
if N == Reverse :
    print(" It is a Palindrome:",N)
else:
    print(" It is Non Palindrome:",N)

# 4.1 normal method for all programs
def Palindrome(N):
    Temp = N
    rev = 0
    while N > 0:
        digit = N%10
        rev = rev*10+digit
        N = N//10
    if Temp == rev:
        print("Its Is a Palindrome :", Temp)
    else:
        print("It isn't Palindrome :", Temp)
N = int(input())
Palindrome(N)


""" 5. Python Program to Reverse a Number """
def reverse_number(N):
    if N < 10 :
        return N
    else:
        last_digit = N%10
        remaining_number = N//10
        reversed_number = reverse_number(remaining_number)
        return int(str(last_digit) + str(reversed_number))

N = int(input("Enter the Number:"))
reversed_number = reverse_number(N)
print("Reversed Number :", reversed_number)
