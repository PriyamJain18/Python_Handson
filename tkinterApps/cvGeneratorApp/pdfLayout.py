from tkinter import *
from tkinter import messagebox
from genCV import cvGenerator

def on_generate_cv_click():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    website = website_entry.get()
    skills = skills_text.get("1.0", END).strip().split('\n')
    education_lines = education_text.get("1.0", END).strip().split('\n')
    experience_lines = experience_text.get("1.0", END).strip().split('\n')

    educationList = []
    experienceList = []
    for education in education_lines:
        degree, university = education.split(':')
        educationList.append({'degree': degree.strip(), 'university': university.strip()})

    for experience in experience_lines:
        job_title, description = experience.split(':')  
        experienceList.append({'job_title': job_title.strip(), 'description': description.strip()})

    about = about_text.get("1.0", END).strip()

    if not name or not email or not phone or not address or not website or not skills or not educationList or not experienceList:
        messagebox.showerror(message='Please fill in all the details')
        return

    cv = cvGenerator()
    cv.create_qrcode(website)
    cv.generate_CV(name, email, phone, address, website, skills, educationList, experienceList, about)

window = Tk()
window.title("CV Generator")

name_label = Label(window, text="Name: ")
name_label.pack()
name_entry = Entry(window)
name_entry.pack()

email_label = Label(window, text="Email: ")
email_label.pack()
email_entry = Entry(window)
email_entry.pack()

phone_label = Label(window, text="Phone: ")
phone_label.pack()
phone_entry = Entry(window)
phone_entry.pack()


address_label = Label(window, text="Address: ")
address_label.pack()
address_entry = Entry(window)
address_entry.pack()


website_label = Label(window, text="Website: ")
website_label.pack()
website_entry = Entry(window)
website_entry.pack()

skills_label = Label(window, text="Skills:(Enter one skill per line) ")
skills_label.pack()
skills_text = Text(window, height=5, width=30)
skills_text.pack()  

education_label = Label(window, text="Education:(Enter one per line in format 'Degree':'University') ")
education_label.pack()
education_text = Text(window, height=5, width=30)
education_text.pack()

experience_label = Label(window, text="Experience:(Enter one per line in format: 'JobTitle', 'Description') ")
experience_label.pack()
experience_text = Text(window, height=5, width=30)
experience_text.pack()

about_label = Label(window, text="About Me: ")
about_label.pack()
about_text = Text(window, height=5, width=30)
about_text.pack()

button = Button(window, text="Generate CV", command=on_generate_cv_click)
button.pack()

window.mainloop()