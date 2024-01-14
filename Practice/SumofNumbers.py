lst = [1,2,5,6,7,9,56]
totalSum = 0
#for o in range(0,len(lst)):
o = 0
while o < len(lst):
     totalSum = totalSum + lst[o]
     o += 1
print(totalSum)



def Sum(set):
    sum = 0
    # for i in set:
    i = 1
    while i < len(set):
        sum += set[i]
        i += 1
    print(sum)
set = {'1' : 2,'2' : 3,'3' : 4,'4' : 5}
#Sum(set)
sum = 0
for i in set:
    sum = sum + set[i]
print(sum)

