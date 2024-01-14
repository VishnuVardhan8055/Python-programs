# dictionary = {"key1": "value1", "key2": "value2"}
# for key, value in dictionary.items():
#     print(key, value)
# Student_marks={'john':23, 'mike':43, 'henna':34}
# print(max(Student_marks))
# i=0
# for key,value in Student_marks.items():
#     if value > i:
#         i = value
# print(i)
# dictionary = {"key1": 10, "key2": 20, "key3": 30}
#
# max_value = None
#
# for key, value in dictionary.items():
#     if max_value is None or value > max_value:
#         max_value = value
#
# print(max_value)

dictionary = {"key1": 10, "key2": 69, "key3": 30}

max_value = None

for key in dictionary.keys():
    if max_value is None or dictionary[key] > max_value:
        max_value = dictionary[key]

print(max_value)



