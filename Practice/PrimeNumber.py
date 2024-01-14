def prime(n):
    if 0 >= n == 1:
        print("Prime is must grater than 1")
    else:
        for i in range(2,n//2+1):
            if n%i == 0:
                return False
        return True
n = int(input())
prime(n)
for i in range(2,n+1):
    if(prime(i)):
        print(i,end=" ")
