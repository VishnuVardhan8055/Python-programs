""" To Check isIsomorphic Strings """
S = input()
T = input()
Zipped = set(zip(S,T))
if (len(Zipped)) == (len(set(S))) == (len(set(T))):
    print(True)
else:
    print(False)
