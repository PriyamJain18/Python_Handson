from tkinter import *
from tkinter import ttk
import psycopg2
from tkinter import messagebox

# Run a database query and return the results
def run_query(query, parameters=()):
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    query_result = None
    try:
        cur.execute(query,parameters)
        if query.lower().startswith("select"):
            query_result = cur.fetchall()
        conn.commit()
    except psycopg2.Error as e:
        Message.showerror("Database Error", str(e))
    finally:
        cur.close()
        conn.close()
    return query_result

# Refresh the treeview with current data from the database
def refresh_treeview():
    students = run_query("select * from students;")
    for item in tree.get_children():
        tree.delete(item)
    if students:
        for student in students:
            tree.insert('', 'end', values=student)


def insert_student():
    query = "insert into students (name, address, age, number) values (%s, %s, %s, %s)"
    parameters = (name_entry.get(), address_entry.get(), age_entry.get(), number_entry.get())
    run_query(query, parameters)
    messagebox.showinfo("Success", f"Student {name_entry.get()} added successfully")
    refresh_treeview()

def delete_student():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Selection Error", "No student selected")
        return
    values = tree.item(selected, 'values')
    student_id = values[0]
    query = "delete from students where student_id=%s"
    run_query(query, (student_id,))
    messagebox.showinfo("Success", f"Student ID {student_id} deleted successfully")
    refresh_treeview()

def update_student():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Selection Error", "No student selected")
        return
    values = tree.item(selected, 'values')
    student_id = values[0]
    query = "update students set name=%s, address=%s, age=%s, number=%s where student_id=%s"
    parameters = (name_entry.get(), address_entry.get(), age_entry.get(), number_entry.get(), student_id)
    run_query(query, parameters)
    messagebox.showinfo("Success", f"Student ID {student_id} updated successfully")
    refresh_treeview()

def create_table():
    query = "create table if not exists students(student_id serial primary key, name text, address text, age int, number text);"
    run_query(query)
    messagebox.showinfo("Success", "Student table created successfully")

root = Tk()
root.title("Student Database Management System")

# Create a frame for the student data input
frame = LabelFrame(root, text="Student Data", padx=10, pady=10)
frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

# Input fields for student data
# Name, Address, Age, Number
Label(frame, text="Name: ").grid(row=0, column=0,padx=2, pady=2, sticky='w')
name_entry = Entry(frame, width=30)
name_entry.grid(row=0, column=1, sticky='ew', pady=2)

Label(frame, text="Address: ").grid(row=1, column=0,padx=2, pady=2, sticky='w')
address_entry = Entry(frame, width=30)
address_entry.grid(row=1, column=1, sticky='ew', pady=2)

Label(frame, text="Age: ").grid(row=2, column=0,padx=2, pady=2, sticky='w')
age_entry = Entry(frame, width=30)
age_entry.grid(row=2, column=1, sticky='ew', pady=2)

Label(frame, text="Number: ").grid(row=3, column=0,padx=2, pady=2, sticky='w')
number_entry = Entry(frame, width=30)
number_entry.grid(row=3, column=1, sticky='ew', pady=2)

# Buttons for various operations
# Create Table, Add Student, Update Student, Delete Student
button_frame = Frame(root)
button_frame.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
Button(button_frame, text="Create Table").grid(row=0, column=0, padx=5, pady=5) 
Button(button_frame, text="Add Student", command=insert_student).grid(row=0, column=1, padx=5, pady=5) 
Button(button_frame, text="Update Student", command=update_student).grid(row=0, column=2, padx=5, pady=5) 
Button(button_frame, text="Delete Student",command=delete_student).grid(row=0, column=3, padx=5, pady=5) 

# View Students Data
tree_frame = Frame(root)
tree_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y) 

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
tree.pack()
tree_scroll.config(command=tree.yview)  
tree['columns'] = ("Student ID", "Name", "Address", "Age", "Number")
tree.column("#0", width=0, stretch=NO) #hide the first empty column
tree.column("Student ID", anchor=W, width=80) #anchor is alignment, 'W' is center
tree.column("Name", anchor=W, width=120)
tree.column("Address", anchor=W, width=120) 
tree.column("Age", anchor=W, width=50)
tree.column("Number", anchor=W, width=120)

tree.heading("#0", text="", anchor=W)
tree.heading("Student ID", text="Student ID", anchor=W)
tree.heading("Name", text="Name", anchor=W)
tree.heading("Address", text="Address", anchor=W)
tree.heading("Age", text="Age", anchor=W)
tree.heading("Number", text="Number", anchor=W)


refresh_treeview()
root.mainloop()