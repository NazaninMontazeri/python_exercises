from persian_tools import digits

lesson_list = [
    {"name" : "data mining" , "unit" :  3 , "teacher" : "ali"},
    {"name" : "python" , "unit" :  5 , "teacher" : "fateme"},
    {"name" : "math" , "unit" :  3 , "teacher" : "reza"},
    {"name" : "sci" , "unit" :  2 , "teacher" : "sogol"},
    {"name" : "math" , "unit" :  3 , "teacher" : "ahmad"}
]

new_lesson_1 ={"name" : "math" , "unit" :  3 , "teacher" : "reza"}
new_lesson_2 = {"name" : "math" , "unit" :  3 , "teacher" : "sogol"}
new_lesson_3 ={"name" : "python" , "unit" :  5 , "teacher" : "fateme"}

#لیستی از درس های جدید
new_lessons = [new_lesson_1 , new_lesson_2 , new_lesson_3]
print(new_lessons)

student_lesson_list = []

#جستجو درس های جدید با لیست درسا
student_lesson_list = list(filter(lambda new_lesson : new_lesson in lesson_list , new_lessons))
print( "student list :" , student_lesson_list)

#مرتب سازی بر اساس تعداد واحد
def sorting_tedad_unit(lesson):
    return lesson["unit"]
result = sorted(student_lesson_list , key = sorting_tedad_unit ,reverse = True)
print("sorting unit :" , result)

#مرتب سازی اسم درسا بر  اساس حروف الفبا
def sorting_alefba(lesson):
    return lesson["name"]
result = sorted(student_lesson_list , key = sorting_alefba , reverse = True)
print("sorting name :" , result)

#اضافه کردن قیمت به هر عضو
def add_price(lesson):
    if lesson["unit"] == 2 :
        lesson["price"] = 1000
    elif lesson["unit"] == 3 :
        lesson["price"] = 1200
    elif lesson["unit"] == 5 :
        lesson["price"] = 1400
    return lesson

student_lesson_list = list(map(add_price , student_lesson_list ))
print(student_lesson_list)

#مبلغ کل پرداختی به حروف
price = list(map(lambda lesson : lesson["price"] , student_lesson_list))
print("price list :" , price)

sum_price = sum(price)
print("sum price : " , sum_price)

print(digits.convert_to_word(sum_price))