import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QComboBox, QLabel, QMessageBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowTitle('Combo Activated')


        # Widgets
        self.output = QLabel('Output')

        self.combo = QComboBox()
        self.combo.addItem('Option 1')
        self.combo.addItem('Option 2')
        self.combo.addItem('Option 3')
        self.combo.addItem('Option 4')
        # activated[str] - holt sich den Inhalt des aktiven Items der Combobox
        self.combo.activated[str].connect(self.change)
        # activated[int] - holt sich die Stelle des aktiven Items der Combobox
        self.combo.activated[int].connect(self.change2)


        # Layout
        vBox = QVBoxLayout()
        vBox.addWidget(self.combo)
        vBox.addWidget(self.output)

        self.setLayout(vBox)
        self.show()

    def change(self, txt):
        self.output.setText(txt)


    def change2(self, stelle):
        print('Item an Pos: ', stelle+1)

# Hauptprogramm
app = QApplication(sys.argv)
w = Window()

sys.exit(app.exec_())
