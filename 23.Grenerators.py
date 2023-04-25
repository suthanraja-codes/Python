

li = []

def fun(num):
    for i in num:
        li.append(i)
    return li

num = [1,2,3,4,5,9,67,7]
print(fun(num))

def fun1 (num1):

    for i in range (1,num1+1):
       yield i*i

fun2 = fun1(10)
for i in  fun2:
    print(i)





