from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem,QPushButton, QLineEdit, QSpinBox, QDockWidget, QFormLayout, QMainWindow, QWidget, QApplication, QTableWidget
import sys
from PyQt6.QtCore import Qt
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("products.db")
        self.createTable()
        self.initUI()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName TEXT,
                lastName TEXT,
                age INTEGER
                )
        """)
        self.conn.commit()

    def initUI(self):        
        self.setGeometry(0,0,1300,600)
        #Creating table
        self.customerDetails = ["id","firstName", "lastName", "age"]
        row = 0
        column = 0
        self.table = QTableWidget()
        self.table.setColumnCount(len(self.customerDetails))
        
        #set table heading
        self.table.setHorizontalHeaderLabels(self.customerDetails)
        self.view_customer()
        
          
        #creating dock widget where input form lies
        dock = QDockWidget()
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        #creating customer form
        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.firstName = QLineEdit(form)
        self.lastName = QLineEdit(form)
        self.age = QSpinBox(form, minimum=18, maximum=60)
        

        #adding form elements to layout
        layout.addRow("First Name", self.firstName)
        layout.addRow("Last Name", self.lastName)
        layout.addRow("Age", self.age)
       

        add_button = QPushButton("Add Customer")
        add_button.clicked.connect(self.add_customer)
        layout.addRow(add_button)

        update_button = QPushButton("Update Customer")
        update_button.clicked.connect(self.add_customer)
        layout.addRow(update_button)
        
        delete_button = QPushButton("Delete Customer")
        delete_button.clicked.connect(self.delete_customer)
        layout.addRow(delete_button)


        dock.setWidget(form)
        self.setCentralWidget(self.table)

    #Method to add customer to table
    def add_customer(self):
        #row = self.table.rowCount()
        firstName = self.firstName.text().strip()
        lastName = self.lastName.text().strip()
        age = self.age.text().strip()
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO products (firstName, lastName, age) VALUES (?,?,?)', (firstName, lastName, age))
        self.conn.commit()
        self.view_customer()

    def view_customer(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products')
        customers = cursor.fetchall()
        self.table.setRowCount(len(customers))

        print(customers)
        for row, cust in enumerate(customers):
            for col, value in enumerate(cust):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row,col,item)
                
        
    def update_customer(self):
        current_row = self.table.currentRow()
        if current_row <0 or current_row>=self.table.rowCount():
            return QMessageBox.warning(self, "No row selected")
 
        firstName = self.firstName.text().strip()
        lastName = self.lastName.text().strip()
        age = self.age.text().strip()
        cust_id = int(self.table.item(current_row,0).text())
        button = QMessageBox.question(self,"Update Customer", "Do you want to update", QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Cancel)
      
        if button == QMessageBox.StandardButton.Yes:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE products  SET firstName=?, lastName=?, age=? WHERE id=?",(firstName, lastName, age, cust_id))
            self.conn.commit()

        self.view_customer()

    def delete_customer(self):
        current_row = self.table.currentRow()
        if current_row <0 or current_row>=self.table.rowCount():
            return QMessageBox.warning(self, "No row selected")

        button = QMessageBox.question(self,"Delete Customer", "Do you want to delete", QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Cancel)
        cust_id = int(self.table.item(current_row,0).text())
        if button == QMessageBox.StandardButton.Yes:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM products WHERE id=?",(cust_id,))
            self.conn.commit()
        self.view_customer()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()