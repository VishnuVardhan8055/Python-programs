Strs = ["flower", 'flat', 'flow']
res = ""
for a in zip(*Strs):
    if len(set(a)) == 1:
        res += a[0]
    else:
        print(res)
print(res)
print(set(zip(*Strs)))

