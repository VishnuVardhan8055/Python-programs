N = int(input())
a = 0
b = 1
if N == 0 or N < 0 :
    print('no fabinoci of 0 & negative Values')
elif N > 0:
    for i in range(1,N):
        c = a + b 
        a = b
        b = c
        print(c,end = ' ')
print(b)
 
def Fibonacci(N) :
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else :
        return Fibonacci(N-1) + Fibonacci(N-2)

print(Fibonacci(9))

# A recursive function to find nth catalan number
def catalan(n):
	# Base Case
	if n <= 1:
		return 1

	# Catalan(n) is the sum of catalan(i)*catalan(n-i-1)
	res = 0
	for i in range(n):
		res += catalan(i) + catalan(n-i-1)

	return res


# Driver Program to test above function
for i in range(10):
	print(catalan(i), end='  ')
