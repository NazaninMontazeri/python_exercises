# اعتبارسنجی اطلاعات کاربر
#برنامه اصلی
from validate_module import *

while True:
    option = show_menu()

    match option:
        case 1 :
            id_number = input("Enter national id :")
            national_id(id_number)

        case 2 :
            pass

        case 3 :
            pass

        case 4 :
            pass

        case 5 :
            pass

        case 0:
            break

        case _ :
            print("invalid option!!!!!")