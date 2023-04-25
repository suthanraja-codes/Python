
dict = {'name':'suthan','age':21,'from':'mukkudal'}
print(dict)
print(dict['name'])

# Adding New Pair
dict['to']='tenkasi'
print(dict)

# Modify
dict['age']=20
print(dict)

# Delete

del dict['to']
print(dict)

# Looping

for key,value in dict.items():
    print(key)
    print(value)

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

for key in sorted(dict.keys()):
    print(key)


l1 = []
l2 = {'name':'king','age':21,'class':'maths'}
l1.append(l2)

l3={'name':'blue','age':20,'class':'eee'}
l1.append(l3)
print(l1)
print(l1[0])
print(l1[0]['name'])