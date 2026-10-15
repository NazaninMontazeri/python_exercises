#ساخت کلاس انسان با استفاده از getter و setter

class Person:
    #متد سازنده
    def __init__(self , name , n_id , phone = None , address = None):
        self.name = name
        self.n_id = n_id
        self.phone = phone
        self.address = address

    #متد نمایش رشته ای شی
    def __repr__(self):
        return f"Person(name={self.name} , n_id={self.n_id})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , new_name):
        if not isinstance(new_name , str):
            raise TypeError("Name must be string")
        self.__name = new_name

    @property
    def n_id(self):
        return self.__n_id

    @n_id.setter
    def n_id(self , new_n_id):
        if not isinstance(new_n_id , int):
            raise TypeError("N id must be integer")
        self.__n_id = new_n_id