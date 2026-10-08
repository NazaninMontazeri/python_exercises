#کلاس برقی
from practice_21.product import Product

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