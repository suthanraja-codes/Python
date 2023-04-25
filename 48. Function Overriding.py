class employee:

    def workingHrs(self):
        self.hrs = 50

    def printall(self):
        print("Total Working Hrs : " ,self.hrs)

class trainee(employee):

    def workingHrs(self):
        self.hrs = 60

    def resetHrs(self):
        super().workingHrs()

o = employee()
o.workingHrs()
o.printall()

t = trainee()
t.workingHrs()
t.printall()
t.resetHrs()
t.printall()

