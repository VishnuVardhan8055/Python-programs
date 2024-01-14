# # def make_first_letter_capital(string):
# #   """
# #   This function takes a string as input and returns a new string with the first letter capitalized.
# #
# #   Args:
# #     string: The string to be capitalized.
# #
# #   Returns:
# #     A new string with the first letter capitalized.
# #   """
# #
# #   first_letter = string[0].upper()
# #   rest_of_string = string[1:]
# #   new_string = first_letter + rest_of_string
# #   return new_string
# #
# #
# # def main():
# #   """
# #   This function tests the make_first_letter_capital function.
# #   """
# #
# #   string = input("")
# #   new_string = make_first_letter_capital(string)
# #   print(new_string)
# #
# #
# # if __name__ == "__main__":
# #   main()
# #
# def function(string):
#   """Capitalizes the first letter of every word in a string.
#
#   Args:
#     string: The string to capitalize.
#
#   Returns:
#     The capitalized string.
#   """
#
#   words = string.split(" ")
#   capitalized = []
#   for word in words:
#     capitalized_words = word[0].upper() + word[1:]
#     capitalized.append(capitalized_words)
#
#   capitalized_string = " ".join(capitalized)
#   return capitalized_string
#
#
# def main():
#   string = input("Enter a string: ")
#   capitalized_string = function(string)
#   print(capitalized_string)
#
#
# if __name__ == "__main__":
#   main()
str = input()
print(str.title())
