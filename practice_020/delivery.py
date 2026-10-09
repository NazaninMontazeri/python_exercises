#ساخت کلاس تحویل
class Delivery :

    # متد سازنده
    def __init__(self):
        self.id = None
        self.name = None
        self.delivary_date = None
        self.address = None

    #متد بروزرسانی
    def update(self):
        print(f"UPDATED:{self.id} {self.name} {self.delivary_date} {self.address}")

    #متد نمایش رشته ای شی
    def __repr__(self):
        return f"Delivary(id={self.id} , name= {self.name} , delivary_date= {self.delivary_date} , address= {self.address})"