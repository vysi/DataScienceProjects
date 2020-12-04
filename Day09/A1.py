import random


class Wetter:
    beschreibung = ['Sonne', 'Regen', 'Schnee']
    def __init__(self):
        self.beschreibung = random.choice(Wetter.beschreibung)
        self.wind = random.randint(0, 25)
        self.temp = self.createTemp()

    def createTemp(self):
        if self.beschreibung == 'Schnee':
            return random.randint(-15, 0)
        else:
            return random.randint(0, 37)

    def vorhersage(self):
        print(f'Es herrscht {self.beschreibung}, bei {self.temp} Grad und {self.wind}km/h Windgeschwindigkeit')

    def __str__(self):
        return str(self.beschreibung)


w = Wetter()
w.vorhersage()
print(w)
