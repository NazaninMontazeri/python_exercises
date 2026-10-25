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
Label(window , text="phone").place(x = 20 , y = 20)
check_phone_number = StringVar()
Entry(window , textvariable = check_phone_number).place(x = 110 , y = 20)

#national_id
Label(window , text="national_id").place(x = 20 , y = 60)
national_id = StringVar()
Entry(window , textvariable = national_id).place(x = 110 , y = 60)

#card_number
Label(window , text="card_number").place(x = 20 , y = 100)
check_card_number = StringVar()
Entry(window , textvariable = check_card_number).place(x = 110 , y = 100)

#plate
Label(window , text="plate").place(x = 20 , y = 140)
check_car_plate= StringVar()
Entry(window , textvariable =  check_car_plate).place(x = 110 , y = 140)


window.mainloop()