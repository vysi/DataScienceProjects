class Klasse:
    classvariable = 0
    def __init__(self, x):
        # classvariable = 0
        self.instanzvariable = x
        Klasse.classvariable += 1
        self.__unsichtbar = 'Unsichtbar'

    # methode, welche sich immer auf eine Instanz (ein Objekt)
    # bezieht
    def changeIV(self, x):
        self.instanzvariable = x

    # methode, welche sich auf eine Klasse bezieht
    # unabhängig vom Objekt
    @classmethod
    def getCV(cls):
        print(cls.classvariable)

    # methode, welche unabhängig von Klasse und Objekt ist
    @staticmethod
    def summe(x, y):
        return x + y


class Klasse2(Klasse):
    classvariable = 0
    def __init__(self):
        Klasse.__init__(self, 'Hallo')
        # super().__init__(self, 'Hallo')
        Klasse2.classvariable += 1


print(Klasse.classvariable)

obj1 = Klasse('Hallo')
print(Klasse.classvariable)
obj2 = Klasse('Welt')

print(Klasse.classvariable)
print(obj1.classvariable)

print(obj1.instanzvariable)
print(obj2.instanzvariable)
obj2.changeIV('Welt!')
print(obj2.instanzvariable)

Klasse.getCV()
obj2.getCV()

print(obj2.summe(3, 4))
print(Klasse.summe(3, 4))

print(obj2._Klasse__unsichtbar)


obj3 = Klasse2()

obj3.getCV()
Klasse2.getCV()
