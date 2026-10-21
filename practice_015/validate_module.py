# توابع مورد نیاز

from persian_tools.national_id import *
from persian_tools.phone_number import *
from persian_tools.bank.card_number import *
from persian_tools.plate import *
from persian_tools.bill import *

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
    if validate(id_number):
        return True
    else:
        print("invzlid national id ...")
        return False

#تابع موبایل
def phone_number(phone):
    if validate(phone):
        print(operator_data(phone))
        return True
    else:
        print("invzlid phone number ...")
        return False

#تابع شماره کارت بانکی
def card_number(card_num):
    if validate(card_num):
        print(bank_data(card_num))
        return True
    else:
        print("invzlid card number ...")
        return False

#تابع پلاک
def car_plate(plate):
    if is_valid(plate):
        return True
    else:
        print("invzlid car plate ...")
        return False
#تابع شناسه قبض

