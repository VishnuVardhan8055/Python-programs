N = int(input("Enter the Size of List:"))
lst = [int(x) for x in input("enter the elements:").split()[:N]]
Total_Sum = 0
for i in range(0,len(lst)):
    Total_Sum += lst[i]
mean = Total_Sum / len(lst)
print(mean)