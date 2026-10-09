#تعریف کلاس درس با شی گرایی

#کلاس درس
class Lesson :

    #متد دریافت اطلاعات
    def __init__(self):
        self.code = None
        self.name = None
        self.teacher = None

    #متد ذخیره
    def save(self):
        print(f"Saved :{self.code} {self.name} {self.teacher}")

    #متد ویرایش
    def edit(self):
        print("Edited")

    #متد نمایش رشته ای شیء
    def __repr__(self):
        return f"Lesson(code={self.code} , name={self.name} , teacher={self.teacher})"