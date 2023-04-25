# Encapsulation


class student:
    def __init__(self, total):
        self._total = total

    def avg(self):
        return self._total / 5.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self,t):
        self._total =t

o = student(400)
print(o.total)
print(o.avg())

o.total = 390
print(o.total)
print(o.avg())
