from PyQt6.QtWidgets import QInputDialog, QFileDialog, QMainWindow, QMenu, QMenuBar, QTextEdit, QComboBox, QFormLayout, QLineEdit, QWidget, QApplication, QPushButton, QLabel, QCheckBox
import sys
from PyQt6.QtGui import QAction, QTextCursor, QColor
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Notepad')
        self.setGeometry(100,100,400,400)

        self.edit_field = QTextEdit(self)
        self.setCentralWidget(self.edit_field)
        self.set_current_file = None

        #Creating menu bar
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        menuBar.setNativeMenuBar(False)

        #Adding File Menu and its actions
        fileMenu = QMenu("File", self)
        menuBar.addMenu(fileMenu)

        new_action = QAction("New",self)
        fileMenu.addAction(new_action)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("Open", self)
        fileMenu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save", self)
        fileMenu.addAction(save_action)
        save_action.triggered.connect(self.save_file)
        
        saveAs_action = QAction("Save As", self)
        fileMenu.addAction(saveAs_action)
        saveAs_action.triggered.connect(self.saveAs_file)

        #Adding edit menu and its actions
        editMenu = QMenu("Edit", self)
        menuBar.addMenu(editMenu)

        undo_action = QAction("Undo",self)
        editMenu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action = QAction("Redo", self) 
        editMenu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        cut_action = QAction("Cut", self)
        editMenu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        copy_action = QAction("Copy", self)
        editMenu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)

        paste_action = QAction("Paste", self)
        editMenu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        find_action = QAction("Find", self)
        editMenu.addAction(find_action)
        find_action.triggered.connect(self.find_text)

    def new_file(self):
        print('creating new file')
        self.edit_field.clear()
        self.set_current_file = None

    def open_file(self):
        print('opening a  file')
        filepath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files(*);; Python Files(*.py)")
        with open(filepath, "r") as file:
            text = file.read()
            self.edit_field.setText(text)

    def saveAs_file(self):
        print('saving a  file')
        filepath,_ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files(*);; Python File(*.py)")
        if filepath:
            with open(filepath, "w") as file:
                file.write(self.edit_field.toPlainText())
            self.set_current_file = filepath

    def save_file(self):
        print('saving a  file as')
        if self.set_current_file:
            with open(self.set_current_file,"w") as file:
                file.write(self.edit_field.toPlainText())
        else:
            self.saveAs_file()
        QFileDialog.getSaveFileName

    def find_text(self):
        print("find")
        search_text,ok = QInputDialog.getText(self, "Find text", "Search for ")
        if ok:
            all_words = []
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)
            Highlight_color = QColor(Qt.GlobalColor.yellow)
            while (self.edit_field.find(search_text)):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(Highlight_color)

                selection.cursor = self.edit_field.textCursor()
                all_words.append(selection)
            self.edit_field.setExtraSelections(all_words)

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
