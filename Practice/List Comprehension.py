# Find all of the numbers from 1–1000 that are divisible by 8
numbers = [i for i in range(1,1001) if i % 8 == 0 ]
print(*numbers)

# Find all of the numbers from 1–1000 that have a 6 in them
#nums = [num for  num in range(1,1001)]
result = [i for i in range(1,1001) if "6" in str(i)]
print(*result)

# Count the number of spaces in a string
string = "Hello Vishnu Vardhan this is Your MacBook AirM1"
result = len([i for i in string if i ==' '])
print(result)

# Remove all of the vowels in a string
string = " An Ant will be Come a king the world "
result = "".join([char for char in string if char  not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']])
# Count all of the vowels in a string
count = len([j for j in string  for i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] if j == i ])
print(result)
print(count)

# Find all of the words in a string that are less than 5 letters
Data = " Any thing that in your life is to get Your Hard-work & Smart-work "
#Data = string.split(" ")
result = [i for i in Data.split() if len(i) < 5]
print(*result)

# Use a dictionary comprehension to count the length of each word in a sentence
String = " Hello Mac Book Air M1 User"
result = {Str:len(Str) for Str in String.split()}
print(result)

# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
#divisible_numbers = [num for num in range(1, 1001) if (num % div == 0 for div in range(2, 10))]
divisible_numbers = [num for num in range(1,1001) if True in [True for divisor in range(2,10) if num % divisor == 0]]
print(divisible_numbers)

# For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by
result = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in range(1,1001)}
print(result)
print(result)


def highest_single_digit_divisor(number):
  """Returns the highest single digit divisor of a number."""
  for divisor in range(1, 10):
    if number % divisor == 0:
      return divisor
  return None

results = {
  number: highest_single_digit_divisor(number)
  for number in range(1, 1001)
}

highest_single_digit = max(results.values())
print(f"The highest single digit any of the numbers from 1 to 1000 is divisible by is {highest_single_digit}.")
