'''Represents the Nom class, which holds integers as fractions with
nominator and denominator and contains math methods for +, /, *'''
class Nom:
    def __init__(self, nominator):
        try:
            isinstance(nominator, int)
        except Exception as E:
            raise Exception("Input number not int")

        self.nominator = nominator
        self.denominator = 1

    def add(self, nom):
        if self.denominator == nom.denominator:
            self.nominator += nom.nominator
        else:
            self.nominator = (self.nominator * nom.denominator) + (nom.nominator * self.denominator)
            self.denominator = self.denominator * nom.denominator

    def multi(self, nom):
        self.nominator *= nom.nominator
        self.denominator *= nom.denominator

    def div(self, nom):
        self.nominator *= nom.denominator
        self.denominator *= nom.nominator

    def flip(self):
        nom = self.nominator
        dem = self.denominator
        self.nominator = dem
        self.denominator = nom

    def print(self):
        print('nom:', str(self.nominator) + '/' + str(self.denominator))

    def get_value(self):
        if (self.nominator / self.denominator).is_integer():
            return str(int(self.nominator / self.denominator))
        else:
            return str(self.nominator) + '/' + str(self.denominator)