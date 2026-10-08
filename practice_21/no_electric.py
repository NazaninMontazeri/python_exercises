# کلاس غیر برقی
from practice_21.product import Product

class NoElectric(Product) :

    # متد سازنده
    def __init__(self):
        self.weight = None

#کلاس مبلمان
class Ferniture(NoElectric) :

    # متد سازنده
    def __init__(self):
        self.capacity = None
        self.color = None

#test
fer1 = Ferniture()
fer1.name = "ferniture"
fer1.capacity = "7"
fer1.color = "red"
fer1.price = "2340$"

print(fer1)