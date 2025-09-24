from fpdf import FPDF
import pyqrcode

class cvGenerator(FPDF):
    def header(self):
        self.image('mywebsite.png', 10,8,25,title="Protfolio Site")

    def footer(self):
        pass

    def generate_CV(self, name, email, phone, address, website, skills, education, experience, about):
        self.add_page()
        self.ln(20)

        #Displaying name
        self.set_font("Arial","B",20)
        self.cell(0,10,name,new_x="LMARGIN", new_y="NEXT",align="C")

        #Displaying contact information
        self.set_font("Arial","B",12)
        self.cell(0,10,"Contact Information",new_x="LMARGIN", new_y="NEXT",align="L")

        self.set_font("Arial","",10)
        self.cell(0,5,"Email: {}".format(email),new_x="LMARGIN", new_y="NEXT",align="L")
        self.cell(0,5,"Phone number: {}".format(phone),new_x="LMARGIN", new_y="NEXT",align="L")
        self.cell(0,5,"Address: {}".format(address),new_x="LMARGIN", new_y="NEXT",align="L")

        self.ln(15)

        #Displaying skills
        self.set_font("Arial","B",12)
        self.cell(0,10,"Skills",new_x="LMARGIN", new_y="NEXT",align="L")
        self.set_font("Arial","",10)
        for skill in skills:
            self.cell(0,5,"- {}".format(skill),new_x="LMARGIN", new_y="NEXT",align="L")

        self.ln(15)

        #Displaying Experience
        self.set_font("Arial","B",12)
        self.cell(0,10,"Work Experience",new_x="LMARGIN", new_y="NEXT",align="L")
        self.set_font("Arial","",10)
        for exp in experience:
            self.cell(0,5,"{}: {}".format(exp['job_title'], exp['description']),new_x="LMARGIN", new_y="NEXT",align="L")

        self.ln(15)
        
        #Displaying Education
        self.set_font("Arial","B",12)
        self.cell(0,10,"Education",new_x="LMARGIN", new_y="NEXT",align="L")
        self.set_font("Arial","",10)
        for edu in education:
            self.cell(0,5,"{}: {}".format(edu['degree'], edu['university']),new_x="LMARGIN", new_y="NEXT",align="L")

        self.ln(15)

        #Displaying About me
        self.set_font("Arial","B",12)
        self.cell(0,10,"About me",new_x="LMARGIN", new_y="NEXT",align="L")
        self.set_font("Arial","",10)
        self.multi_cell(0,5,about,new_x="LMARGIN", new_y="NEXT",align="L")


        self.output("CV.pdf")

    def create_qrcode(self,website):
        qrcode = pyqrcode.create(website)
        qrcode.png('mywebsite.png', scale=6)