a = [12, 14, 16, 17, 4, 2]
for i in range(len(a)):
    value = a[i]
    print(i, value)

print(a[3])

print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))
