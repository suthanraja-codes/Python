class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def msg(self):
        return self.name + " Age is " + str(self.age) + " years old"


obj = student('suthan', 21)
print(obj.name)
print(obj.age)
print(obj.msg)

obj.age = 20
print(obj.msg)
