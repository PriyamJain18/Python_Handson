from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
import sys
from PyQt6.QtGui import QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle('User Input')
        self.setGeometry(0,0,400,400)

        name_label = QLabel(self)
        name_label.setText("Enter your name")
        name_label.move(40,10)

        self.name = QLineEdit(self)
        self.name.resize(200,20)
        self.name.move(130,10)

        button = QPushButton(self)
        button.setText('click')
        button.move(60, 40)
        button.clicked.connect(self.buttonClicked)
        
        self.result_label = QLabel(self)
        self.result_label.setText("")
        self.result_label.setFixedSize(120,120)
        self.result_label.move(60,70)

    def buttonClicked(self):
        print('Your name is : '+self.name.text())
        self.result_label.setText('You name is '+self.name.text())

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
