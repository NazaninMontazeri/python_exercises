#برنامه اصلی
from practice_13.parking_module import *

while True :
    #گرفتن گزینه
    option = show_menu()
    print("_________________________________________")

    match option :

        case 1:
            #دریافت اطلاعات ماشین
            car = get_car_info()

            #بررسی تکراری نبودن پلاک
            if find_car_by_plate(parking_list ,car['plate']) :
                print("Duplicate car error")
            else:
                parking_list.append(car)
                print("Car added successfully")

        #چاپ پارکینگ لیست
        case 2 :
            print("parking list :",parking_list)

        #جستجو ماشین با پلاک
        case 3 :
            plate = input("Enter a plate:")
            result = find_car_by_plate(parking_list, car['plate'])
            if result :
               print("Car found:", result )
            else:
                print("Car not found")

        # خارج شدن
        case 0 :
            break

        # اشتباه وارد کردن گزینه
        case _ :
            print("Invalid option , try again")
    print("_________________________________________")