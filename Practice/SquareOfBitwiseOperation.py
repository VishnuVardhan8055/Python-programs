def binary_power(binary_number, power):
  """
  This function takes a binary number as input and returns its power raised to the given power.

  Args:
    binary_number: The binary number to be converted.
    power: The power to which the binary number should be raised.

  Returns:
    The power of the binary number raised to the given power.
  """
  binary_number = binary_number[::-1]
  power_of_two = 1
  integer_value = 0
  for digit in binary_number:
    integer_value += int(digit) * (power_of_two ** power)
    power_of_two *= 2
  return integer_value
if __name__ == "__main__":
  binary_number = "1010"
  power = 2
  print(binary_power(binary_number, power))

