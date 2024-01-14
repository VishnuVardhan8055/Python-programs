# def count_of_lines(path):
#     with open(path, 'r') as f:
#         line_count = (f.readlines())
#     return line_count
# path = "Text.txt"
# count_of_lines(path)
import os
def count_number_of_lines_in_text_file(file_path):

  # Open the text file in read mode.
  with open(file_path, "r") as f:
    # Count the number of lines in the text file.
    line_count = len(f.readlines())

  # Return the number of lines in the text file.
  return line_count


def count_number_of_lines_in_text_file_by_file_name(file_name):


  # Get the path to the text file.
  file_path = os.path.join(os.getcwd(), file_name)

  # Count the number of lines in the text file.
  number_of_lines = count_number_of_lines_in_text_file(file_path)

  # Return the number of lines in the text file.
  return number_of_lines


# Example usage:

file_name = "Text.txt"

number_of_lines = count_number_of_lines_in_text_file_by_file_name(file_name)

print(f"The number of lines in the text file {file_name} is {number_of_lines}.")


