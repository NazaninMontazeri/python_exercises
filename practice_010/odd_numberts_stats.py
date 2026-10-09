# تا وقتی کاربر عدد صفر وارد نکرده عدد بگیره و چاپ میانگین اعداد فرد
odd_list = []
odd_sum = 0

#بررسی عدد وارد شده صفر است یا خیر
while True :
    num = int(input("enter a number:"))
    if num == 0 :
        break
    else:
        if num % 2 != 0 :
            odd_list.append(num)
            odd_sum += num

#چاپ لیست اعداد فرد
print("odd numbers list:" , odd_list)

#چاپ جمع اعداد فرد
print("sum odd numbers:" , odd_sum)

# محاسبه میانگین اعداد فرد
odd_avg = odd_sum / len(odd_list)

#چاپ میانگین اعداد فرد
print("avrage odd numbers:" , odd_avg)