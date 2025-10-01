from PyQt6.QtWidgets import QMainWindow, QTextEdit, QComboBox, QFormLayout, QLineEdit, QWidget, QApplication, QPushButton, QLabel, QCheckBox
import sys
from PyQt6.QtGui import QAction

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menu')
        self.setGeometry(100,100,400,400)

        #Toolbar
        toolbar = self.addToolBar("Main Toolbar")
        self.newAction = QAction("New")
        toolbar.addAction(self.newAction)

        self.saveAction = QAction("Save")
        toolbar.addAction(self.saveAction)


        #Menu bar
        #Step 1
        menubar = self.menuBar()

        #Step 2 - menu
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")

        #Step 3 - actions to file menu
        self.new = QAction("New")
        self.exit = QAction("Exit")
        file_menu.addAction(self.new)
        file_menu.addAction(self.exit)

        file_menu.addSeparator()

        #Step 3 - actions to edit menu
        self.copy = QAction("Copy")
        self.cut = QAction("Cut")
        self.paste = QAction("Paste")
        edit_menu.addAction(self.copy)
        edit_menu.addAction(self.cut)
        edit_menu.addAction(self.paste)

        edit_menu.addSeparator()

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
