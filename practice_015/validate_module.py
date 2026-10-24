# توابع مورد نیاز

from persian_tools import national_id as nid
from persian_tools import phone_number as phone
from persian_tools import bank
from persian_tools import plate
from persian_tools import bill



#تابع منو
def show_menu():
    print("1) Enter a national id")
    print("2) Enter a phone")
    print("3) Enter a card number")
    print("4) Enter a plate number")
    print("5) Enter a bill id")
    print("0) Exit")
    option = int(input("Enter a option :"))
    return option

#تابع کد ملی
def national_id(id_number):
    if nid.validate(id_number):
        return True
    else:
        print("invzlid national id ...")
        return False

#تابع موبایل
def check_phone_number(phone_num):
     if phone.validate(phone_num):
        print(phone.operator_data(phone_num))
        return True
     else:
        print("invalid phone number ...")
        return False

#تابع شماره کارت بانکی
def check_card_number(card_num):
    if bank.card_number.validate(card_num):
        print(bank.card_number.bank_data(card_num))
        return True
    else:
        print("invzlid card number ...")
        return False

#تابع پلاک
def check_car_plate(plate_num):
    if plate.is_valid(plate_num):
        print(plate.get_info(plate_num))
        return True
    else:
        print("invzlid car plate ...")
        return False

#تابع شناسه قبض
def check_bill_id(bill_number , payment_number):
    if bill.get_detail(bill_number , payment_number):
       print(bill.get_detail(bill_number , payment_number))
       return True
    else:
        print("invzlid bill id ...")
        return False