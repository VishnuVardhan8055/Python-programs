""" To check the given element is vowel r not"""
def Vowels(given_element):
    lst = ['a', 'e', 'i', 'o', 'u']
    if given_element in lst:
        print("it is ovwel", given_element)
    else:
        print("It is not a ovwel", given_element)
data = input()
given_element = data
Vowels(given_element)

""" find the number of vowels in a given word"""
input = input()
vowels = 'aeiou'
count = 0
for i in input:
    if i in vowels:
        count += 1
print("no.of vowels in word:",count)



