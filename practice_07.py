#تا وقتی کاربر کلمه exit وارد نکرده اسم بگیرد و به ترتیب الفبا یکی یکی چاپ کند
name_list = []

# بررسی اسم ایا برابر exit ست یا خیر
while True :
    name = input("enter a name:")
    if name.lower() != "exit" :
        name_list.append(name)
        print(name_list)
    else:
       break

# چاپ لیست کل اسم ها
print("name list:",name_list)

# ترتیب کردن اسم ها به ترتیب الفبا
name_list.sort()

# چاپ اسم ها یکی یکی
for name in name_list:
   print("name:", name)