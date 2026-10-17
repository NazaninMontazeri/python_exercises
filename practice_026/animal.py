#ساخت کلاس حیوان با استفاده از ارث بری و چند ریختی
class Animal :
    def __init__(self , name):
        self.name = name

    def __repr__(self):
        return f"Animal(name = {self.name})"

    def make_sound(self):
        pass

class Cow(Animal) :
    def make_sound(self):
        print("MOO")

class Dog(Animal) :
    def make_sound(self):
        print("woof")