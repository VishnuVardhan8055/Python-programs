def roman_to_int(roman_numeral):
  roman_numeral_map = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
  }
  result = 0
  previous_value = None
  for current_value in roman_numeral:
    if previous_value is not None and current_value > previous_value:
      result -= 2 * roman_numeral_map[previous_value]
    result += roman_numeral_map[current_value]
    previous_value = current_value
  return result


def main():
  roman_numeral = input("Enter a Roman numeral: ")
  integer = roman_to_int(roman_numeral)
  print("The integer value of the Roman numeral is:", integer)
if __name__ == "__main__":
  main()
