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
        print("invzlid id ...")
        return False

#تابع موبایل


#تابع شماره کارت بانکی


#تابع پلاک


#تابع شناسه قبض

