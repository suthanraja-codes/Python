class details:
    name = 'suthan'
    age = 21


# get attribute

print(getattr(details, 'name'))
print(getattr(details, 'age'))
print(getattr(details, 'from', 'mukkudal'))

# .notation

print(details.name)
print(details.age)

# set attribute
setattr(details, 'to', 'tenkasi')
print(details.to)

# set attribute . notation

details.cls = 'maths'
print(details.cls)

# delattribute

delattr(details, 'cls')
print(details.__dict__)

del details.to
print(details.__dict__)
