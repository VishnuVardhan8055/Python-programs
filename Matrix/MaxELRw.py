# Matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# list = []
# for row in Matrix:
#     max_ele = max(row)
#     list.append(max_ele)
# print(list)

#
# data = [[1, 1, 1],
#         [0, 1, 0],
#         [0, 1, 1]]
# j = 0
# ls = []
# for i in range(0, 3):
#     count = 0
#     while j < 3:
#         if data[i][j] == 1:
#             count += 1
#         j += 1
#     ls.append(count)
# print(ls)

# data = [[1, 1, 1],
#         [0, 1, 0],
#         [0, 1, 1]]
# j = 0
# ls = []
# for i in range(0, 3):
#     count = 0
#     da = []
#     for j in range(0, 3):
#         if data[i][j] == 1:
#             count += 1
#     da.append(count)
# ls.append(da)
# print(ls)
# print(max(ls))

data = [[1, 1, 1],
        [0, 1, 0],
        [0, 1, 1]]

# # Count the number of 1's in each row using list comprehension
# row_counts = [sum(1 for x in row if x == 1) for row in data]
#
# # Print the maximum value in the list
# print(row_counts)

row_counts = []
for row in data:
    count = 0
    for x in row:
        if x == 1:
            count += 1
    row_counts.append(count)
print(max(row_counts))


def find_highest_number_of_1s_in_column(d):
  """Finds the highest number of 1's in a column in a Python list.

  Args:
    data: A Python list of lists.

  Returns:
    The highest number of 1's in a column.
  """

  # Create a list comprehension expression to calculate the number of 1's in
  # each column.
  column_counts = [sum(1 for x in col if x == 1) for col in zip(*d)]

  # Return the highest number of 1's in a column.
  return (column_counts)


# Example usage:

d = [[1, 1, 1],
        [1, 1, 0],
        [0, 1, 1]]

highest_number_of_1s_in_column = find_highest_number_of_1s_in_column(d)

print(highest_number_of_1s_in_column)


