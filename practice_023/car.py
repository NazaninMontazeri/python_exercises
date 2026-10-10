#ساخت کلاس ماشین با استفاده getter و setter

class Car :
    #متد سازنده
    def __init__(self , name , color , plate):
        self.name = name
        self.color = color
        self.plate = plate

    #متد نمایش رشته ای شی
    def __repr__(self):
        return f"Car(name={self.name} , color={self.color} , plate={self.plate})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , new_name):
        if not isinstance(new_name , str):
            raise TypeError("Name must be a string")
        self.__name = new_name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self , new_color):
        if not isinstance(new_color , str):
            raise TypeError("Color must be a string")
        self.__color = new_color

    @property
    def plate(self):
        return self.__plate

    @plate.setter
    def plate(self , new_plate):
        if not isinstance(new_plate , str):
            raise TypeError("Plate must be a string")
        self.__plate = new_plate