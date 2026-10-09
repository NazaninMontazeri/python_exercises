#میانگین اعداد زوج سه رقمی بخش پذیر بر عدد 7
even_count = 0
even_sum = 0

#بررسی اعداد سه رقمی زوج و بخش پذیر بر عدد 7
for num in range(100 , 999 , 2):
    if num % 7 == 0 :
        even_count += 1
        even_sum += num

# محاسبه میانگین
even_avg = even_sum / even_count

#چاپ میانگین
print("even average:",even_avg)
