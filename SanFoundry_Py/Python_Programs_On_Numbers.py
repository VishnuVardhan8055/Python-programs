""" 1. Python Program to Find Prime Numbers in a Given Range """
Num = int(input("Enter a Range :"))
for i in range(2,Num+1):
    k = 0
    for j in range(2,i//2+1):
        if i % j == 0:
            k = k + 1
    if k<=0:
        print(i)


""" 2. Python Program to Check Prime Number """
num = int(input("Enter a Number to Check Weather it is Prime or Not : "))
k = 0
for i in range(2,num//2+1):
    if num % i  == 0:
        k = k + 1
if k >= 0:
    print(True)
else:
    print(False)


""" 3. Python Program to Check Armstrong Number """
num = int(input("Enter the number :"))
#length = len(str(num))
c = []
for i in str(num):
    a = int(i) ** 3 #len(str(num))
    c.append(a)
b = sum(c)
if num == b:
    print("True")
else:
    print("False")

# 3.1 Python Program to Check Armstrong Number
num = int(input("Enter the number :"))
a = list(map(int,str(num)))
b = list(map(lambda x:x**3,a))
if sum(b)==num:
    print("True")
else:
    print("False")


""" 4. Python Program to Check the Strong Number """
num = int(input("Enter the number "))
sum1=0
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")
