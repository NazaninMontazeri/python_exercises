#تعریف کلاس درس با شی گرایی

#کلاس درس
class Lesson :

    #تابع دریافت اطلاعات
    def __init__(self):
        self.code = None
        self.name = None
        self.teacher = None

    #تابع ذخیره
    def save(self):
        print(f"Saved :{self.code} {self.name} {self.teacher}")

    #تابع ویرایش
    def edit(self):
        print("Edited")

    #تابع نمایش رشته ای شیء
    def __rep__(self):
        return f"Lesson(code={self.code} , name={self.name} , teacher={self.teacher})"

