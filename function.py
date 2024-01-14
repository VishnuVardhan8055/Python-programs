"""
def Data(college_name , year):
    print(f'{college_name},{year}')
Data('Aitsk',3)

"""

"""
#---> Functional Arguments
# @---> 1.  Required Postional Arguments
def Func(a,b,c,d):
    print(f'a={a},b={b},c={c},d={d}')
Func(11,22,33,44)
# @---> 2.  Default Arguments
def Deflt(a,b,c,d=100):
    print(f'a={a},b={b},c={c},d={d}')
Deflt(12 , 13 ,14 , 55)
# @---> 3. Keyword Arguments
def Kywrd(a=0,b=0,c=0,d=0):
    print(f'a={a},b={b},c={c},d={d}')
Kywrd(c=20,a=111,d=222,b=777)
# @---> 4. Arbitary Arguments
def Arbtry(*a):
    for i in a:
        print(i,end=' ')
Arbtry(1, 2 ,3 ,4 ,5 ,6)


"""
def Change(lst):
    lst[1] =100
lst =[ 1,22,33,44]
Change(lst)
print(lst)
result = lst.index(33)
print(result)





