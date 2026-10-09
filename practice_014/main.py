#برنامه اصلی
from practice_014.contact_module import *

while True :
    #گرفتن گزینه ها
    option = show_menu()
    print("__________________________________")

    match option :

        case 1 :
            #دریافت اطلاعات کالا
            contact = get_contact_info()

             #بررسی تکراری نبودن کال ا
            if find_contact_by_phone(contact_list , contact['phone']) :
                print("Duplicate contact error")
            else:
                 contact_list.append(contact)
                 print("Contact added successfully")

        # چاپ لیست کالا
        case 2 :
            print("Contact list:" , contact_list)

        #جستجو و تکراری نبودن کالا
        case 3 :
            phone = input("Enter a phone:")
            result = find_contact_by_phone(contact_list , contact["phone"])
            if result :
                print("Contact found:", result)
            else:
                print("Contact not found")

        #خارج شدن
        case 0 :
            break

        #اشتباه واردن کردن گزینه
        case _ :
            print("Invalid option , try again")
    print("__________________________________")