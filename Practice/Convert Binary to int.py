def binary_to_int(binary_number):
  """
  This function takes a binary number as input and returns its integer representation.
  Args:
    binary_number: The binary number to be converted.
  Returns:
    The integer representation of the binary number.
  """
  binary_number = binary_number[::-1]
  power_of_two = 1
  integer_value = 0
  for digit in binary_number:
    integer_value += int(digit) * power_of_two
    power_of_two *= 2
  return integer_value

if __name__ == "__main__":
  binary_number = "1011"
  print(binary_to_int(binary_number))





