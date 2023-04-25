
# Multileval Inheritance

class grandpa:

    def ownHouse(self):
        print("Grandpa's House")

class father(grandpa):

    def ownBike(self):
        print("Own's Bike")

class son(father):

    def ownBook(self):
        print("Own's Book")

o = son()
o.ownBook()
o.ownHouse()
o.ownBike()