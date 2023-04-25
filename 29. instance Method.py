class student:
    name = 'suthan'
    age = 21

    def all(self,gender):
        print("Name   : ", student.name)
        print("Age    : ", student.age)
        print("Gender : ",gender)

obj = student()

"""
obj.all()

student.all(obj)
"""

obj.all("male")
print("------------------------------------------------------------------------")
student.all(obj,'male')

