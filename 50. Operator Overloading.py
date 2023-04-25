class addition:

    def __init__(self,a):
        self.a = a

    def __add__(val_1, val_2):
        return val_1.a+val_2.a

class subtraction:
    def __init__(self,b):
        self.b = b

    def __sub__(o1, o2):
        return o1.b-o2.b

class multiplication:
    def __init__(self,m):
        self.m = m
    def __mul__(m1,m2):
        return m1.m * m2.m


val = addition(10)
val1 = addition(5)
print(val+val1)

b1 = subtraction(12)
b2 = subtraction(4)
print(b1 - b2)

m3 = multiplication(3)
m4 = multiplication(5)
print(m3*m4)