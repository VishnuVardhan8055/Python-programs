# import os
# def check_file_exists(file_name):
#   """Checks if a file exists.
#
#   Args:
#     file_name: The name of the file to check.
#
#   Returns:
#     True if the file exists, False if it does not.
#   """
#   for root, directories, files in os.walk('.'):
#     for file in files:
#       if file_name == file:
#         return True
#   return False
#
# if __name__ == "__main__":
#   file_name = input("Enter the file name to check: ")
#   if check_file_exists(file_name):
#     print("The file exists.")
#   else:
#     print("The file does not exist.")
# import os
# import pathlib
# def Check_file(File_name):
#     for root,directories,files in os.walk('.'):
#         for file in files:
#             if File_name == file:
#                 print("File Exits at :",{os.path.join(root, file)})
#                 return True
#     return False
# if __name__ == "__main__":
#     File_name = input("Enter the File Name :")
#     if Check_file(File_name):
#         a = os.walk(File_name)
#         print("The File Exits ")
#     else:
#         print("The File not Exits")
import os

for root, directories, files in os.walk('.'):
  for file in files:
    print(file)

