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
            pass

        case 4 :
            pass

        case 5 :
            pass

        case 0:
            print("Bye")
            break

        case _ :
            print("invalid option!!!!!")