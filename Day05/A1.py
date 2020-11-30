def hello(x):
    print(f'Hello {x}!')
class Konto:
    def __init__(self, inh, stand):
        self.inhaber = inh
        self.__kontostand = stand

    def einzahlen(self, x):
        if x > 0:
            self.__kontostand += x

    def abbuchen(self, x):
        if x <= self.__kontostand:
            self.__kontostand -= x
            # self.kontostand = self.kontostand - x

    def einsicht(self):
        return self.__kontostand

    def __str__(self):
        return self.inhaber

    def hello(self):
        hello(self.inhaber)

if __name__ == '__main__':
    konto = Konto('Jan', 100)

    konto.einzahlen(50)

    print(konto.einsicht())
    konto.abbuchen(20)
    print(konto.einsicht())
    print(konto._Konto__kontostand)

    print(konto)
    konto.hello()
