import psycopg2
 
def open_db_connection():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    return conn

def close_db_connection(conn):
    conn.commit()
    conn.close()

def create_table():
    conn = open_db_connection()
    conn.cursor.execute("create table students(student_id serial primary key, name text, address text, age int, number text);")
    print('Student table created')
    close_db_connection(conn)

def get_student():
    name = input('Enter Student name :')
    address = input('Enter address :')
    age = input('Enter age :')
    number = input('Enter number :')
    return name,address,age,number

def insert_student():
    name,address,age,number = get_student()
    conn = open_db_connection()
    conn.cursor().execute("insert into students (name, address, age, number) values (%s, %s, %s, %s)", (name, address, age, number))
    print(f"Student {name} inserted in student table")
    close_db_connection(conn)

def read_students():
    conn = open_db_connection()
    cur = conn.cursor()
    cur.execute("select * from students;")
    students = cur.fetchall()
    for student in students:
        print(f"ID: {student[0]}, Name:{student[1]}, Address:{student[2]} Age:{student[3]}, Number:{student[4]}")
    conn.close()

def update_all_student_fields():
    student_id = input("Enter id of the student to be updated")
    name,address,age,number = get_student()
    conn = open_db_connection()
    conn.cursor().execute("update students set name=%s, address=%s, age=%s, number=%s where student_id=%s",(name, address,age,number,student_id))
    print(f"Student details updated!!")
    close_db_connection(conn)

def update_one_student_field():
    student_id = input("Enter id of the student to be updated: ")
    fields = {
        "1":("name", "Enter name: "),
        "2":("address", "Enter address: "),
        "3":("age", "Enter age: "),
        "4":("number", "Enter number: ")
    }
    print("Which field would you like to update: ")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    field_choice = input("Enter the number of the field you want to update: ")
    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        new_field_value = input(prompt)
        conn = open_db_connection()
        sql = f"update students set {field_name}=%s where student_id=%s"
        conn.cursor().execute(sql,(new_field_value, student_id))
        print(f"For student {student_id} field {field_name} is updated with value {new_field_value}")
        close_db_connection(conn)
    else:
        print("Invalid data provided")

def delete_student():
    student_id = input("Enter the ID of the student you want to delete: ")
    conn = open_db_connection()
    cur = conn.cursor()
    cur.execute("select * from students where student_id=%s",(student_id,))
    student = cur.fetchone()
    if student:
        print(f"Student to be deleted: ID {student[0]}, Name {student[1]}")
        choice = input("Are you sure you want to delete the student? (y/n)")
        if choice.lower() == 'y' :
            cur.execute("delete from students where student_id=%s",(student_id))
            print(f"Student {student[1]} deleted successfully.")
        else:
            print("Deletion cancelled")
    else:
        print("Invalid input")
    close_db_connection(conn)

print("Welcome to the student database management system\n")
while True:
    print("\nWhat do you want to do?\n1.Create Table\n2.Insert Student\n3.Dsiplay All Students\n4.Update All Fields of A Student\n5.Update One Field of A Student\n6.Delete A Student\n7.Exit")
    choice = input("Enter your choice (1-7): ")
    if(choice == "1"):
        create_table()
    elif(choice == '2'):
        insert_student()
    elif(choice == '3'):
        read_students()
    elif(choice=='4'):
        update_all_student_fields()
    elif(choice=='5'):
        update_one_student_field()
    elif(choice=='6'):
        delete_student()
    elif(choice=='7'):
        break
    else:
        print("Invalid choice, please enter a number between (1-7)")
