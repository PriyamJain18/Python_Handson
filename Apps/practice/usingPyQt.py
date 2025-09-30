from PyQt6.QtWidgets import QWidget, QApplication, QLabel
import sys
from PyQt6.QtGui import QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('my first pyqt window')
        self.setGeometry(0,0,400,400)

        with open('mycar.png'):
            image_lable = QLabel(self)
            pixmap = QPixmap('mycar.png')
            image_lable.setPixmap(pixmap)
            image_lable.move(50,0)

        #car name
        name_label = QLabel(self)
        name_label.setFont(QFont("Arial", 20))
        name_label.setText('My Car')
        name_label.move(170,170)

        #engine spec
        engine_label = QLabel(self)
        engine_label.setFont(QFont("Arial", 16))
        engine_label.setText('Engine Capacity 4L TFSI')
        engine_label.move(20,210)

        #features
        features_label = QLabel(self)
        features_label.setFont(QFont("Arial", 16))
        features_label.setText('Features: ABS, EBD, ADAS')
        features_label.move(20,240)

        #models
        models_label = QLabel(self)
        models_label.setFont(QFont("Arial", 16))
        models_label.setText('Models: 2.2 Petrol, 1.8 Diesel')
        models_label.move(20,270)

        #pricing
        pricing_label = QLabel(self)
        pricing_label.setFont(QFont("Arial", 16))
        pricing_label.setText('$80,000')
        pricing_label.move(20,2 70)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
