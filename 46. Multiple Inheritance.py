# Multiple Inheritance

class father:

    def fishing(self):
        print("Fishing In Rivers")

    def chess(self):
        print("Playing Chess In Father")

class mother:

    def cook(self):
        print("Cooking Food")

    def chess(self):
        print("Playing Chess In Mother")

class son(father,mother):

    def cycling(self):
        print("Riding The Cycle")

o = son()
o.cycling()
o.fishing()
o.cook()
o.chess()