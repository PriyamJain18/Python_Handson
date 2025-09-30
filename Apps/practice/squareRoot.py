from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QLineEdit
import sys, math
from PyQt6.QtGui import QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.total = 0.0
        self.setWindowTitle('Square Root of the number is :')
        self.setGeometry(0,0,400,400)

        label = QLabel(self)
        label.setText("Enter a number")
        label.move(200,20)

        self.number = QLineEdit(self)
        self.number.move(200,60)

        calculate_button = QPushButton(self)
        calculate_button.setText('Calculate Square Root')
        calculate_button.move(200,100)
        calculate_button.clicked.connect(self.squareRoot)

        self.result_label = QLabel("Result: ", self)
        self.result_label.move(200,140)
        self.result_label.resize(200,20)

    def squareRoot(self):
        try:
            num = float(self.number.text())
            result = math.sqrt(num)
            if result.is_integer():
                self.result_label.setText('Square root : ' +str(result))
            else:
                msg = QMessageBox.warning(self, "Not a Perfect square", "This number is not a perfect square")
        except ValueError:
            QMessageBox.warning(self, "Invalid input", "Please enter a valid number")

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
