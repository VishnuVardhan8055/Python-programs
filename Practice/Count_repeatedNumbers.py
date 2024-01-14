# list_numbers = [1, 2, 3, 1, 2, 5, 1, 3]
# number_of_1s = 0
# for number in list_numbers:
#   if number == 1:
#     number_of_1s += 1
# print(number_of_1s)

# def favourite_singers(n, playlist):
#
#   frequency_of_singers = {}
#   favourite_singers = 0
#
#   for song in playlist:
#     frequency_of_singers[song] = frequency_of_singers.get(song, 0) + 1
#
#   favourite = max(frequency_of_singers.values())
#
#   for value in frequency_of_singers.values():
#     if value == favourite:
#       favourite_singers += 1
#
#   return favourite_singers
#
#
# if __name__ == "__main__":
#   n = int(input())
#   playlist = list(map(int, input().split()))
#
#   print(favourite_singers(n, playlist))

# from collections import Counter
# songs = int(input())
# singer_input = str(input()).split(" ")
# play_list_count = list(Counter(singer_input).values())
# max_count = max(play_list_count)
# print(play_list_count.count(max_count))

from collections import Counter
n = int(input())
list = list(int(i) for i in input().split()[:n])
count = Counter(list)
print(count)
print(max(count.values()))

