#کلاس برقی
from practice_021.product import Product

class Electric(Product) :

    # متد سازنده
    def __init__(self):
        self.voltage = None

#کلاس لبتاپ
class Laptab(Electric) :

    # متد سازنده
    def __init__(self):
        self.ram = None
        self.cpu = None

#کلاس موبایل
class Mobile(Electric) :

    # متد سازنده
    def __init__(self):
        self.sreen_size = None

#کلاس ایفون
class Iphone(Mobile) :

    # متد سازنده
    def __init__(self):
        self.serial = None

#کلاس سامسونگ
class Samsung(Mobile) :

    # متد سازنده
    def __init__(self):
        self.serial = None

#test
mob1 = Samsung()
mob1.name = "A21"
mob1.screen_size = "8"
mob1.voltage = "220"
mob1.price = "1200$"

print(mob1)