# اعتبارسنجی اطلاعات کاربر
#برنامه اصلی
from validate_module import *

while True:
    option = show_menu()

    match option:
        case 1 :
            id_number = input("Enter national id :")
            national_id(id_number)
            print("Function returned:", national_id(id_number))

        case 2 :
            phone = input("Enter phone number :")
            check_phone_number(phone)
            print("Function returned:", check_phone_number(phone))

        case 3 :
            card_number = input("Enter card number :")
            check_card_number(card_number)
            print("Function returned:", check_card_number(card_number))

        case 4 :
            plate = input("Enter card number :")
            check_car_plate(plate)
            print("Function returned:", check_car_plate(plate))

        case 5 :
            pass

        case 0:
            print("Bye")
            break

        case _ :
            print("invalid option!!!!!")