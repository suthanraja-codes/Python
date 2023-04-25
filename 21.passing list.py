
#
# def fun(list):
#     for i in list:
#         print(i.title())
#
# names = ["suthan","king","queen"]
# fun(names)


# def fun(list):
#     for i in range (0,len(list)):
#         list[i] = list[i].title()
#         print(list[i])
# names = ["king","blue","green"]
# fun(names)
# print(names)


def fun(list):
    for i in range(0,len(list)):
        list[i]=list[i].title()
        print(list[i])
names = ["suthan","mr blackshadow","blue"]
fun(names[:])
print(names)

# Returning Dictionary

def fun():
    name ={'name' :"suthan",'age':20}
    return name

print(fun())