from abc import ABC, abstractmethod

class reserveBank(ABC):

    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def credit(self):
        pass

    @abstractmethod
    def  debit(self):
        pass

class HDFC(reserveBank):

    def loan(self):
        print("We Provides 26.% Loan Amount")

    def credit(self):
        print("hdfc Provides credit")

    def debit(self):
        print("hdfc provides debit")

    def card(self):
        print("hdfc provides card")

o = HDFC()
o.credit()
o.loan()
o.debit()
o.card()
