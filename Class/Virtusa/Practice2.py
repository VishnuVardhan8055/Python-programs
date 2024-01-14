""" Find the most repeated Letter in a Str """
from collections import Counter
Str = (input())
Data = Counter(Str.lower())
first_value = next(iter(Data.values()))
all_equal = all(value == first_value for value in Data.values())
if all_equal:
    print(first_value)
else:
    print(max(Data.values()))
