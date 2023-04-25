
# Diamond Shape Problem

class A :

    def display(self):
        print(" Class A ")

class B (A):
    def display(self):
        print(" Class B ")

class C (A):
    def display(self):
        print(" Class C ")

class D (B,C):
    def display(self):
        print(" Class D ")

d = D()
d.display()

