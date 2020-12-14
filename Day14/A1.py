import sys
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QRadioButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowTitle('Buttongroup')

        # Widgets
        self.radiolist = []
        self.radios = QButtonGroup()

        for i in range(20):
            b = QRadioButton(f'Radio {i + 1}')
            self.radiolist.append(b)
            self.radios.addButton(b)


        self.radios.buttonClicked.connect(self.button_func)

        self.output = QLabel('Before check!')

        # Layout
        vBox = QVBoxLayout()
        for i in range(len(self.radiolist)):
            vBox.addWidget(self.radiolist[i])

        vBox.addWidget(self.output)

        self.setLayout(vBox)
        self.show()

    def button_func(self):
        self.output.setText('A button was clicked!')

        txt_of_button = self.radios.checkedButton().text()
        self.output.setText(str(txt_of_button))

        #
        # for i in range(len(self.radiolist)):
        #     if self.radiolist[i].isChecked():
        #         self.output.setText(f'Radio {i + 1} was clicked!')
        #         break



# Hauptprogramm
app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())
