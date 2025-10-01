from PyQt6.QtWidgets import QTextEdit, QComboBox, QFormLayout, QLineEdit, QWidget, QApplication, QPushButton, QLabel, QCheckBox
import sys
from PyQt6.QtGui import QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contact Form')
        self.setGeometry(100,100,400,400)
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.subject_combo = QComboBox()
        self.subject_combo.addItems(["Select Subject", "Personal", "Business"])

        self.message_edit = QTextEdit()
  
        self.submit_button = QPushButton()
        self.submit_button.clicked.connect(self.submit_clicked)

        form_layout.addRow(QLabel("Name"), self.name_edit)
        form_layout.addRow(QLabel("Email"), self.email_edit)
        form_layout.addRow(QLabel("Phone"), self.phone_edit)
        form_layout.addRow(QLabel("Subject"), self.subject_combo)
        form_layout.addRow(QLabel("Message"), self.message_edit)
        form_layout.addRow(QLabel("Submit"),self.submit_button)

    def submit_clicked(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()
        subject = self.subject_combo.currentText()
        message = self.message_edit.toPlainText()
        print(name)
        print(email)
        print(phone)
        print(subject)
        print(message)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
