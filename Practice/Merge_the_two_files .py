import os
def merge_files(file1, file2, output_file):
  """Merges two files into a third file.
  Args:
    file1: The path to the first file.
    file2: The path to the second file.
    output_file: The path to the output file.
  """
  with open(file1, "r") as f1:
    with open(file2, "r") as f2:
      with open(output_file, "w") as f3:
        for line in f1:
          f3.write(line)
        for line in f2:
          f3.write(line)
if __name__ == "__main__":
  file1 = "LL.py"
  file2 = "Mean.py"
  output_file = "Merge.txt"
  merge_files(file1, file2, output_file)
