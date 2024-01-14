""" To check the isIsomorphic string """
s = input()
t = input()
ziped = set(zip(s, t))
if len(ziped) == len(s) == len(t):
    print(True)
else:
    print(False)
print(ziped)
print(len(ziped))
