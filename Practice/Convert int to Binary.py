n = int(input())
binary = ''
remainder = 0
while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n //= 2
print(binary)


