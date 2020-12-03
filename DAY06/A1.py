# Create a class School class: attributes: Class level, number of students, class teacher, list of student names.

# (When created, the object is assigned only class level, class teacher and a list of student names).
#
# 1) Create a method that automatically creates the number from the list of students.
# (Defined in the class before the __init__ and called in the __init__)
#
# 2) Instead of assigning strings to students, you should
# student objects are created.
# Students: Attributes: Name, grade level, grades, average
# Create objects for the students. Give them to the school class.
#
# 3) Write a method for the class of students that gets any number of grades and calculates the average.
#
# 4) Write a method for the class class that checks if the grade level of all students matches the grade level of the class. If not, a student should be dismissed from the class.
#
# 5) Write a method for the classroom class that uses the
# Class average Calculated.

class Schoolclass:
    def __init__(self, lehrer, stufe, pupils):
        self.lehrer = lehrer
        self.stufe = stufe
        self.pupils = pupils
        self.anzPupils = self.getPupilNo()

    def getPupilNo(self):
        return len(self.pupils)

    def __str__(self):
        return f'Lehrer: {self.lehrer}, mit {self.anzPupils} Schülern, Klassendurchschnitt: {self.getDurchschnitt()}'

    def getDurchschnitt(self):
        s = 0
        for pupil in self.pupils:
            s += pupil.durchschnitt
        return s/len(self.pupils)

    def testStufe(self):
        newPupils = []
        for pupil in self.pupils:
            if self.stufe == pupil.stufe:
                newPupils.append(pupil)
        self.pupils = newPupils
        self.anzPupils = self.getPupilNo()



class Pupil:
    def __init__(self, name, stufe, marks):
        self.name = name
        self.stufe = stufe
        self.noten = marks
        self.durchschnitt = self.getDurchschnitt()

    def getDurchschnitt(self):
        return sum(self.noten)/len(self.noten)

    def __str__(self):
        return f"{self.name}, {self.durchschnitt}"

hertha = Pupil("Hertha", 5, [1,2,3,4])
bernd = Pupil("Bernd", 6, [2,4,5,3])

klasse1 = Schoolclass('Frau Schmitt', 5, [hertha, bernd])

print(klasse1.getPupilNo())
print(klasse1)

print(bernd)
klasse1.testStufe()
print(klasse1)
