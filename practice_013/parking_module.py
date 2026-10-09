#توابع مورد نیاز

parking_list = []

#تابع منو
def show_menu():
    print("1)Enter to parking")
    print("2)Parking list")
    print("3)Search car by plate")
    print("0)Exit")
    option = int(input("Enter a  option:"))
    return option

#تابع دریافت اطلاعات
def get_car_info() :
    name = input("Enter a name car:")
    color = input("Enter a color car:")
    plate = input("Enter a plate car:")
    enter_time = input("Enter a time:")
    return {'name':name , 'color':color , 'plate':plate , 'enter_time':enter_time}

#تابع نمایش پارکینگ لیست
def print_parking_list(parking_list) :
    for car in parking_list :
        print("Parking List")
        print(f"{car['name']:10} {car['color']:10} {car['plate']:10} {car['enter_time']:10}")

#تابع جستجو و تکراری نبودن
def find_car_by_plate(parking_list , plate) :
   for car in  parking_list :
        if car['plate'] == plate :
            return car
