N = int(input("Enter the Size of a Number:"))
lst = [int(x) for x in input("Enter the list of Elements:").split()[:N]]
Total_Sum = 0
for i in range(0,len(lst)):
    Total_Sum += lst[i]
if len(lst) % 2 == 0:
    median =(len(lst)//2 + len(lst)//2 - 1 ) / 2
else:
    mid = len(lst)//2
    median = lst[mid]
print(median)