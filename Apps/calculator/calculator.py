from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QWidget, QApplication, QPushButton, QLabel, QCheckBox
import sys
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(0,0,150,150)
        self.current_input = "0"
        self.previous_input = ""
        self.current_op = ""

        layout = QGridLayout()
        self.setLayout(layout)

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.display,0,0,1,4)

        buttons = [QPushButton(str(i)) for i in range(10)]
        
        operators = ["+","-","*","/"]
        operator_buttons = [QPushButton(op) for op in operators]

        self.equals_button = QPushButton("=")
        self.equals_button.clicked.connect(self.calculate)
        self.clear_button = QPushButton("C")
        self.clear_button.clicked.connect(self.clear)

        for i,button in enumerate(buttons):
            row,col = divmod(i,3)
            layout.addWidget(button, row+1, col)

        #Adding event handling method for number clicked
        for button in buttons:
            button.clicked.connect(self.number_clicked)

        for i,op_button in enumerate(operator_buttons):
            layout.addWidget(op_button, i+1, 3)

        for op in operator_buttons:
            op.clicked.connect(self.operator_clicked)

        layout.addWidget(self.equals_button, 4,1)
        layout.addWidget(self.clear_button, 4,2)

    def number_clicked(self):
        digit = self.sender().text()

        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        self.display.setText(self.current_input)

    def operator_clicked(self):
        op = self.sender().text()
        if self.current_op == "":
            self.current_op = op
            self.previous_input = self.current_input
            self.current_input = "0"
        else:
            self.calculate()
            self.current_op = op
            self.previous_input = self.current_input
            self.current_input = "0"
       

    def calculate(self):
        if self.current_op =="+":
            result = float(self.previous_input) + float(self.current_input)
        elif self.current_op =="-":
            result = float(self.previous_input) - float(self.current_input)
        elif self.current_op =="*":
            result = float(self.previous_input) * float(self.current_input)
        elif self.current_op =="/":
            if self.current_input == "0":
                result = "Error"
            else:
                result = float(self.previous_input) / float(self.current_input)
        else:
            result = self.current_input
        self.display.setText(str(result))
        self.current_input = result
        self.current_op = ""

    def clear(self):
        self.current_input = "0"
        self.previous_input = "" 
        self.current_op = ""
        self.display.setText(self.current_input)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
