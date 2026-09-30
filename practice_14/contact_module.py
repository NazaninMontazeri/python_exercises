#توابع مورد نیاز

contact = []

#تابع منو
def show_menu():
    print("1)Add contact")
    print("2)Contact list")
    print("3)Search by phone")
    print("0)Exit")
    option = int(input("Enter a  option:"))
    return option

#تابع دریافت اطلاعات
def get_contact_info():
    name = input("Enter a name:")
    last_name = input("Enter a last name:")
    phone = input("Enter a phone:")
    title = input("Enter a title:")
    return {'name':name , 'last_name':last_name , 'phone':phone , 'title':title}

#تابع نمایش اطلاعات

#تابع جستجو و تکراری نبودن شماره تلفن
