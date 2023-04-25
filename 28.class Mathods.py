class Teacher:
    name = 'Blue'
    age = 21

    def all():
        print("Name : ", Teacher.name)
        print("age  : ", Teacher.age)


Teacher.all()

print(Teacher.__dict__)
print(getattr(Teacher, "all"))

getattr(Teacher, "all")()
Teacher.__dict__['all']()
