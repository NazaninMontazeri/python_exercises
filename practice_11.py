#تا زمانی که جمع واحد ها =< 17 واحد است از کاربر درس دریافت کند
unit_sum = 0
lessons_list = []

#دریافت اطلاعات کلاس
while True :
    title = input("enter a title:")
    teacher = input("enter a teacher:")
    duration = int(input("enter a duration:"))
    unit = int(input("enter a unit:"))

    #اضافه کردن به لیست
    lesson = {
        'title':title ,
        'teacher':teacher ,
        'duration':duration ,
        'unit':unit
    }
    lessons_list.append(lesson)

    #چاپ لیست درس
    print("lesson:" , lessons_list)

    #شمارش تعداد واحد ها
    unit_sum += unit

    #بررسی تعداد واحد از 17 بیشتر است یا خیر
    if unit_sum >= 17 :
        break

#چاپ لیست زیر هم و به شکل خواسته شده
for lesson in lessons_list :
    print(f"{lesson['title']:10} by {lesson['teacher']:20} (lesson unit: {lesson['unit']:2}) ")