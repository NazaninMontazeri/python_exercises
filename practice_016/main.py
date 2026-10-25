from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from inquiry_module import *

person_list = []

def verification_click():
    try:
        person = {
            "phone" : check_phone_number(phone.get()) ,
            "card_number" : check_card_number(card_number.get()) ,
            "bill" : check_bill_id(bill.get()) ,
            "national_id" : national_id(national_id.get()) ,
            "plate" : check_car_plate(plate.get())
        }

        person_list.append(person)
        messagebox.showerror("Saved" , "person list")

        national_id.set(0 , 'end.get(')
        phone.set(0 , 'end.get(')
        card_number.set(0 , 'end.get(')
        bill.set(0 , 'end.get(')
        plate.set(0 , 'end.get(')

    except Exception as e :
        messagebox.showerror("Saved" , "person saved")

window = Tk()
window.title("profile")
window.geometry("500x500")

#phone


window.mainloop()