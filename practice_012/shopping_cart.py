#کالا بگیره تا وقتی که جمع کل مبلغ از یک میلیون بیشتر نشود
product_list = []
total_price = 0

#دریافت اطلاعات محصول از کاربر
while True :
    name = input("enter a name:")
    quantity = int(input("enter a quantity:"))
    price = int(input("enter a price:"))

    #اضافه کردن کالا به دیکشنری
    product = {
        "name": name ,
        "quantity" : quantity ,
        "price" : price
    }

    # محاسبه مبلغ کل ا
    total_price += quantity * price

    #چاپ مبلغ کل
    print("total price:" , total_price)

    # بررسی سقف خرید
    if total_price < 1_000_000 :
         #اضافه کردن کالا به لیست
        product_list.append(product)
        print("product saved")
    else:
        print("product max reached")
        break
    print("___________________________________")

#چاپ لیست کالاها
print("product list:" , product_list)

#چاپ لیست کالاها زیر هم و به شکل خواسته شده
for product in product_list :
    print(f"{product['name']:10}{product['quantity']:10}{product['price']:10}")