from tkinter import *

#Lhuhn Algorithm to validate credit card number
def validate_card():
    card_number = card_entry.get()
    if(len(card_number) != 16):
        validate_label.config(text = "Card number must be 16 digits")
        return
    odd_sum = 0
    even_sum = 0
    double_list = []
    card_list = list(card_number)
    for (ind, val) in enumerate(card_list):
        if(ind % 2 != 0):
            odd_sum += int(val) #sum of odd placed digits
        else:
            double_list.append(int(val) * 2)
    
    #sum of double of even placed digits
    double_str = ""
    for x in double_list:
        double_str += str(x)
    
    #converting string to list to sum individual digits
    str_to_list = list(double_str)
    for num in str_to_list:
        even_sum += int(num)

    #final sum of odd and even placed digits
    total_sum = odd_sum + even_sum
    #valid if total_sum is multiple of 10
    if(total_sum % 10 == 0):
        validate_label.config(text = "Valid Card Number")
    else:
        validate_label.config(text = "Invalid Card Number")

root = Tk()

number_label = Label(root, text="Enter Credit Card Number")
card_entry = Entry(root, validate="key", validatecommand=(root.register(lambda char: char.isdigit()), '%S'))
validate_button = Button(root, text="Validate", command=validate_card)

validate_label = Label(root, text="")
validate_label.grid(row=2, columnspan=2, pady=10)

number_label.grid(row=0, column=0, padx=10, pady=10)
card_entry.grid(row=0, column=1, padx=10, pady=10)
validate_button.grid(row=1, columnspan=2, pady=10)  

root.mainloop()