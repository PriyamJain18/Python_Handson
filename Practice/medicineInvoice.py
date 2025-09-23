from tkinter import *
from fpdf import FPDF
 
# Create the main window
window = Tk()
window.title("Invoice Generator")
 
# Initialize variables
medicines = {
    "Medicine A": 10,
    "Medicine B": 20,
    "Medicine C": 15,
    "Medicine D": 25,
    "Medicine E": 30
}
invoice_items = []
total_amount = 0.0
 
# Function to add medicine to the invoice
def add_medicine():
    msg_label.config(text="")
    selected_medicine = medicine_listbox.get(ANCHOR)
    if selected_medicine:
        if quantity_entry.get().isdigit():
            quantity = int(quantity_entry.get())
            price = medicines[selected_medicine]
            item_total = price * quantity
            invoice_items.append((selected_medicine, quantity, item_total))
            total_amount_entry.delete(0, END)
            total_amount_entry.insert(END, str(calculate_total()))
            update_invoice_text()
        else:
            msg_label.config(text="Please enter a valid quantity", fg="red")
    else:
        msg_label.config(text="Please select a medicine", fg="red")
        
# Function to calculate the total amount 
def calculate_total():
    total = 0.0
    for item in invoice_items:
            total += item[2]
    return total
 
# Function to generate and save the invoice as PDF 
def generate_invoice():
    msg_label.config(text="")
    customer_name = customer_entry.get()
    if not customer_name:
        msg_label.config(text="Please enter customer name", fg="red")
        return
    if not invoice_items:
        msg_label.config(text="Invoice is empty", fg="red")
        return
    pdf = FPDF()
    pdf.add_page()
 
    # Set up PDF formatting
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, text="Invoice", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0, 10, text="Customer: " + customer_name,
             new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.cell(0, 10, text="", new_x="LMARGIN", new_y="NEXT")
 
    # Add invoice items to PDF

    with pdf.table(
        borders_layout= "NO_HORIZONTAL_LINES",
        cell_fill_color=(200, 220, 255),
        col_widths=(40, 35, 40, 45),
        line_height=6,
        text_align=("LEFT", "C", "R", "L"),
        width=160
    ) as table:
        row = table.row()
        header = ["Medicine", "Quantity", "Total"]
        for h in header:
            row.cell(h)
        for item in invoice_items:
            row = table.row()
            medicine_name, quantity, item_total = item
            row.cell(medicine_name)
            row.cell(str(quantity))
            row.cell(str(item_total))

        # Add total amount to PDF
    pdf.cell(0, 10, text="Total Amount: " +
             str(calculate_total()), new_x="LMARGIN", new_y="NEXT", align="C")
 
    # Save the PDF file
    pdf.output("invoice.pdf")
 
# Function to update the invoice text
def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(
            END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")

def remove_medicine():
    msg_label.config(text="")
    selected_medicine = medicine_listbox.get(ANCHOR)
    if selected_medicine:
        for item in invoice_items:
            if item[0] == selected_medicine:
                invoice_items.remove(item)
                break
        total_amount_entry.delete(0, END)
        total_amount_entry.insert(END, str(calculate_total()))
        update_invoice_text()
    else:
        msg_label.config(text="Please select a medicine to remove", fg="red")

# GUI layout
medicine_label = Label(window, text="Medicine:")
medicine_label.grid(row =0, column=0, padx=2, pady=2) 
 
medicine_listbox = Listbox(window, selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END, medicine)
medicine_listbox.grid(row=0, column=1, padx=2, pady=2)
 
quantity_label = Label(window, text="Quantity:")
quantity_label.grid( row=1, column=0)
 
quantity_entry = Entry(window)
quantity_entry.grid( row=1, column=1, padx=2, pady=2)
 
add_button = Button(window, text="Add Medicine", command=add_medicine)
add_button.grid(row=2, column=1, padx=2, pady=2)
 
remove_button = Button(window, text="Remove Medicine", command=remove_medicine)
remove_button.grid(row=3, column=1, padx=2, pady=2)

msg_label = Label(window, text="")
msg_label.grid(row=2, column=2, padx=2, pady=2, sticky=E)

total_amount_label = Label(window, text="Total Amount:")
total_amount_label.grid(row=1, column=2, sticky=E)
 
total_amount_entry = Entry(window)
total_amount_entry.grid(row=1, column=3, padx=2, pady=2)
 
customer_label = Label(window, text="Customer Name:")
customer_label.grid(row=6, column=1, sticky=W, padx=2, pady=4)
 
customer_entry = Entry(window)
customer_entry.grid(row=6, column=2, padx=2, pady=4)
 
generate_button = Button(window, text="Generate Invoice", command=generate_invoice)
generate_button.grid(row=6, column=3, padx=2, pady=10)
 
invoice_text = Text(window, height=10, width=50)
invoice_text.grid(row=0, column=2, columnspan=2, padx=2, pady=2)
 
# Start the GUI event loop
window.mainloop()