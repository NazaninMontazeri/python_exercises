#تعریف کلاس ماشین با شی گرایی

#کلاس ماشین
class Car :

    #متد دریافت اطلاعات
    def __init__(self):
        self.name = None
        self.color = None
        self.plate = None

    #متد ذخیره
    def save(self):
        print(F"Saved : {self.name} {self.color} {self.plate}")

    #متد تغییر پلاک
    def change_plate(self):
        print("Changed plate")

    #متد نمایش رشته ای شیء
    def __repr__(self):
        return f"Car(name={self.name} , color={self.color} , plate={self.plate})"