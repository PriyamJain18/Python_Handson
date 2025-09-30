from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel
import sys
from PyQt6.QtGui import QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle('my first pyqt window')
        self.setGeometry(0,0,400,400)

        button = QPushButton(self)
        button.setText('Click')
        button.move(50,50)
        button.clicked.connect(self.buttonClicked)
    
        #adding label to display count
        self.label = QLabel(self)
        self.label.setText(str(self.count))
        self.label.move(100,150)

    def buttonClicked(self):
        self.count +=1
        self.label.setText(str(self.count))
        self.label.adjustSize()


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
