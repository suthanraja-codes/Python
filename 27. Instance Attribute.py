class Student:
    name = 'suthan'
    age = 21


obj = Student()
print(Student.__dict__)
print(obj.__dict__)
print(obj.name)
print(obj.age)

# get attribute


print(getattr(obj, 'name'))
print(getattr(obj, 'age', 29))
obj.course = 'maths'
print(obj.__dict__)
# set attribute

setattr(obj, 'name', 'king')

print(getattr(obj, 'name'))
print(vars(obj))
print(dir(obj))
