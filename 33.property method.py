# Encapsulation


class student:
    def __init__(self, total):
        self._total = total

    def avg(self):
        return self._total / 5.0

    def getter(self):
        return self._total

    def setter(self,t):
        self._total =t

    total = property(getter,setter)

o = student(400)
print(o.total)
print(o.avg())

o.total = 90
print(o.total)
print(o.avg())
