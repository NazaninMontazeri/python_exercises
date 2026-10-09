#تا وقتی کاربر عدد صفر وارد نکرده عدد بگیره و چاپ اعداد زوج و فرد در دو لیست جدا
even_list = []
odd_list = []

#بررسی عدد وارد شده صفر است یا خیر
while True :
    num = int(input("enter a number:"))
    if num == 0 :
        break
    #بررسی عدد زوج یا فرد
    elif num % 2 == 0 :
        even_list.append(num)
    else:
        odd_list.append(num)

#چاپ لیست اعداد زوج و فرد
print("even numbers list:", even_list)
print("odd numbers list:",odd_list)