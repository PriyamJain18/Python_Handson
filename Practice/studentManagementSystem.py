class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.rollNumber = roll_number
        

class School:
    def __init__(self):
        self.students = []
        
    def add_student(self, name, age, rollNumber):
        student = Student(name, age, rollNumber)
        self.students.append(student)
        
    def display_students(self):
        for s in self.students:
            print(f"Student Name: {s.name}, Age: {s.age}, Rollnumber: {s.rollNumber}\n")
            
    def edit_student(self, rollno, new_name, new_age):
        for s in self.students:
            if s.rollNumber == rollno:
                s.name = new_name
                s.age = new_age
                print(f"Student {s.name} Successfully updated")
                
    def delete_student(self, rollno):
        for s in self.students:
            if(s.rollNumber == rollno):
                self.students.remove(s)
                print(f"Student {s.name} delete successfully\n")
                
        
        
school = School()

while True:
    choice = input("Enter your choice: \n1)Add student\n2)Display all students\n3)Edit student data\n4)Delete student data\n5)Quit\n")
    if choice == "1":
        name = input("Enter name of the student")
        age = input("Enter age")
        rollNumber = input("Enter rollNumber")
        school.add_student(name, age, rollNumber)
    elif choice == "2":
        school.display_students()
    elif choice == "3":
        rollno = input('Enter rollno you want to edit')
        new_age = input('enter new age')
        new_name = input('enter new name for the student')
        school.edit_student(rollno, new_name, new_age)
    elif choice == "4":
        rollno = input("Enter roll number you want to delete")
        school.delete_student(rollno)
    elif choice == "5":
        break