import sys
from PyQt5.QtWidgets import *


class Rechner(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowTitle('Zahlentest')

        # Widgets
        self.zahl1 = QLineEdit()
        self.zahl2 = QLineEdit()

        self.plus = QPushButton('+')
        self.plus.clicked.connect(lambda: self.rechnen('+'))
        self.minus = QPushButton('-')
        self.minus.clicked.connect(lambda: self.rechnen('-'))
        self.durch = QPushButton('/')
        self.durch.clicked.connect(lambda: self.rechnen('/'))
        self.mal = QPushButton('*')
        self.mal.clicked.connect(lambda: self.rechnen('*'))

        self.output = QLabel()


        # Layout
        buttons = QVBoxLayout()
        buttons.addWidget(self.plus)
        buttons.addWidget(self.minus)
        buttons.addWidget(self.durch)
        buttons.addWidget(self.mal)

        rahmen = QHBoxLayout()
        rahmen.addWidget(self.zahl1)
        rahmen.addLayout(buttons)
        rahmen.addWidget(self.zahl2)

        final = QVBoxLayout()
        final.addLayout(rahmen)
        final.addWidget(self.output)

        self.setLayout(final)
        self.show()

    def rechnen(self, rechnung):
        if rechnung == '+':
            ergebnis = float(self.zahl1.text()) + float(self.zahl2.text())
        if rechnung == '-':
            ergebnis = float(self.zahl1.text()) - float(self.zahl2.text())
        if rechnung == '/':
            ergebnis = float(self.zahl1.text()) / float(self.zahl2.text())
        if rechnung == '*':
            ergebnis = float(self.zahl1.text()) * float(self.zahl2.text())

        self.output.setText(str(ergebnis))


# Hauptprogramm
app = QApplication(sys.argv)
w = Rechner()
sys.exit(app.exec_())
