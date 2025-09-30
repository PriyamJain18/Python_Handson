from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QCheckBox
import sys
from PyQt6.QtGui import QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.total = 0.0
        self.setWindowTitle('Beverage Cost')
        self.setGeometry(0,0,400,400)

        label = QLabel(self)
        label.setText("Select your options")
        label.resize(200,20)
        label.move(20,20)

        sugar_checkbox = QCheckBox(self)
        sugar_checkbox.setText('Sugar: $0.5')
        sugar_checkbox.move(20,40)
        sugar_checkbox.toggled.connect(self.sugarChecked)

        milk_checkbox = QCheckBox(self)
        milk_checkbox.setText('Milk: $1.5')
        milk_checkbox.move(20,60)
        milk_checkbox.toggled.connect(self.milkChecked)

        self.result_label = QLabel(self)
        self.result_label.setText('Total Cost: $0')
        self.result_label.resize(200,20)
        self.result_label.move(20,90)

    def sugarChecked(self, check):
        if check:
            self.total += 0.5
        else:
            self.total -= 0.5
        self.result_label.setText('Total Cost: $'+ str(self.total))

    def milkChecked(self,check):
        if check:
            self.total += 1.5
        else:
            self.total -=1.5
        self.result_label.setText('Total Cost: $'+ str(self.total))

       

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
