#تعریف کلاس کالا از روی دیاگرام چند سطحی

#کلاس کالا
class Product :

    #متد سازنده
    def __init__(self):
        self.name = None
        self.price = None

    #متد نمایش رشته ای شی
    def __repr__(self):
        return f"Product(name={self.name} , price={self.price})"