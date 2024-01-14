""" 
# @---> Higher-Order Function : 
                                A function that either accept another function as its argument are written another function as return value is aclled Higher-Order Function.

"""
def func1():
    print("Inside the Func1")
    def func2():
        print("Inside the Func2")
        print("Inner Function")
    return func2
f2 = func1()
f2()
"""
Pyhton Provides three popular higher order functions
1. map()
2. filter()
3. Reduce()

# @---> map() :
                The map function calls given function by passing each element from the given sequence and it stores return value for every function call into map object.
                // 1. map() ---> map(function,sequence1,sequence2,---)
            

"""

lst1 = [10 ,20 ,30 ,40 ,50]
lst2 = [1, 2, 3, 4, 5]
#result = list(x**i for x in lst1  for i in lst2  )
res = []
for i in range(len(lst1)):
    res.append(lst1[i] ** lst2[i])

print(res)

list1 = [10, 20, 30, 40, 50]
list2 = [1 ,2 ,3 ,4 ,5]
#result =[lambda list1, list2: list1[i] ** list2[2]  for i in range (len(list1))]
#res = map(result,list1)
#for i in range (len(list2)):
 #   resul(t.append(list2[i] ** list1[i])
res = map(lambda num : list1[i]**list2[i],zip(list1 , list2))
print(list(res))

