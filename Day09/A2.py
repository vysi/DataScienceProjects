import random
class Arbeiter:
    id = 1000
    deps = ['Dev', 'PR', 'HR', 'Sales']
    def __init__(self, name, lohn):
        self.name = name
        self.lohn = lohn
        Arbeiter.id +=1
        self.id = Arbeiter.id
        self.abteilung = random.choice(Arbeiter.deps)

    def abteilungswechsel(self, dep):
        if dep in Arbeiter.deps:
            self.abteilung = dep
        else:
            print('Department not known!')

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Department: {self.abteilung}'

worker1 = Arbeiter('Heinz', 12000)
worker2 = Arbeiter('Helga', 28000)

print(worker1)
print(worker2)
worker2.abteilungswechsel('HR')
print(worker2)
