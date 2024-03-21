# Items = [i for i in input().split()]
# # ItemsAnagram = [''.join(sorted(item)) for item in Items]
# List = []
# for select_item in range(len(Items)):
#     L = []
#     for check_product in range(len(Items)):
#         if Items[select_item] == "".join(sorted(Items[check_product])):
#             List.append(Items[check_product])
#             List.remove(Items[check_product])
#         # else:
#         #     List.insert(0,Items[check_product])
# Items.remove(Items[select_item])
# print(List)
#
#
#
#
# # print(sorted(Items))
# # print(ItemsAnagram)

def group_anagrams(strs):
    anagrams = {}
    for word in strs:
        # Use sorted character counts as a key for anagrams
        key = "".join(sorted(word))
        anagrams.setdefault(key, []).append(word)
    return list(anagrams.values())
# Example usage:
strs = [i for i in input().split()] # ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
