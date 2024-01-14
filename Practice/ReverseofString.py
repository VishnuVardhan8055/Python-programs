# Reverse a Number and String
#  """ $---> for String Reverse """ 
# A = "Hello"
#print(*reversed(A))
# $ ---> method.1

A = int(input())
reverse_number = 0
for i in range(len(str(A))):
    reverse_number = reverse_number * 10 + A % 10
    A //= 10
print(reverse_number)
# $ ---> method.2
B = input()
print(str(B[ : : -1]))
# $ ---> method.3
c = int(input())
Reverse_number = 0
while c > 0:
    Reverse_number = Reverse_number * 10 + c % 10
    c //= 10
print(Reverse_number)

# $ ---> method.4
D = [int(x) for x in input().split()]
E = [int(y) for y in D[: : -1]]
print(E)






