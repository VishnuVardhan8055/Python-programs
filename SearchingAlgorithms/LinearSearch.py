def linearSearch(lst,key):
        for i in range(0,len(lst)):
            if lst[i] == key:
                return True
        return False

lst = [1,3,5,7,9]
key = int(input())
print(linearSearch(lst,key))