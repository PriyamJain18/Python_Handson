from PyQt6.QtWidgets import QFileDialog, QMainWindow, QApplication, QLabel, QStatusBar, QToolBar, QColorDialog
from PyQt6.QtGui import QPixmap, QPainter, QPen, QAction, QIcon
from PyQt6.QtCore import Qt, QPoint, QRect, QSize
import sys, os

class Canvas(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap(600,600)
        self.pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)
        self.drawing = False
        self.last_mouse_pos = QPoint()
        self.status_label = QLabel()
        self.eraser = False
        self.pen_color = Qt.GlobalColor.black
        self.pen_width = 1


    def mouseMoveEvent(self, event):
        mouse_position = event.pos()
        status_text = f"Mouse co-ordinates are:{mouse_position.x(), mouse_position.y()}"
        self.status_label.setText(status_text)
        self.parent.statusBar.addWidget(self.status_label)
        if (event.button and Qt.MouseButton.LeftButton) and self.drawing:
            self.draw(mouse_position)
        pass

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_mouse_pos = event.pos()
            self.drawing = True
        pass

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
        pass

    def draw(self, points):
        painter = QPainter(self.pixmap)
        if self.eraser == False:

            pen = QPen(self.pen_color, self.pen_width)
            painter.setPen(pen)
            painter.drawLine(self.last_mouse_pos, points)
            self.last_mouse_pos = points
        elif self.eraser == True:
            eraser = QRect(points.x(), points.y(), 15,15)
            painter.eraseRect(eraser)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        target_rect = event.rect()
        painter.drawPixmap(target_rect, self.pixmap, target_rect)
        painter.end()


    def selectTool(self, tool):
        if tool == "pencil":
            self.pen_width = 2
            self.eraser = False
        elif tool == "brush":
            self.pen_width = 6
            self.eraser = False
        elif tool == "color":
            color = QColorDialog.getColor()
            self.eraser = False
            self.pen_color = color
        elif tool == "eraser":
            self.eraser = True
        
    def new(self):
        self.pixmap.fill(Qt.GlobalColor.white)
        self.update()

    def save(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", os.path.curdir+"sample.png", "PNG File (*.png)")
        if file_name:
            self.pixmap.save(file_name, "png" )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(400,400)
        self.setWindowTitle("Paint App")

        #creating canvas
        canvas = Canvas(self)
        self.setCentralWidget(canvas)
        #status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        #creating toolbar
        tool_bar = QToolBar("Toolbar")
        tool_bar.setIconSize(QSize(21,21))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea,tool_bar)
        tool_bar.setMovable(False)
        #tool bar icons
        pencil_act = QAction(QIcon("icons/pencil.png"), "Pencil",tool_bar)
        pencil_act.triggered.connect(lambda:canvas.selectTool("pencil"))

        brush_act = QAction(QIcon("icons/brush.png"), "Brush",tool_bar)
        brush_act.triggered.connect(lambda:canvas.selectTool("brush"))

        color_act = QAction(QIcon("icons/color.png"), "Color",tool_bar)
        color_act.triggered.connect(lambda:canvas.selectTool("color"))

        eraser_act = QAction(QIcon("icons/eraser.png"), "Eraser",tool_bar)
        eraser_act.triggered.connect(lambda:canvas.selectTool("eraser"))

        tool_bar.addAction(pencil_act)
        tool_bar.addAction(brush_act)
        tool_bar.addAction(color_act)
        tool_bar.addAction(eraser_act)

        #menubar
        self.new_action = QAction("New")
        self.new_action.triggered.connect(canvas.new)
        self.save_file_action = QAction("Save")
        self.save_file_action.triggered.connect(canvas.save)
        self.quit_action = QAction("Exit")
        self.quit_action.triggered.connect(self.close)
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.save_file_action)
        file_menu.addAction(self.quit_action)
        file_menu.addSeparator()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

