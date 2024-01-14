list = [1, 1, 0, 0, 1, 1, 1]
count = 0
maxcount = 0
for i in range(0, len(list)):
    if list[i] == 1:
      count = count+1
    else:
      if maxcount < count:
        maxcount = count
        count = 0
print(max(maxcount, count))
