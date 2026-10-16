#ساخت کلاس انسان با استفاده از getter و setter

class Person:
    #متد سازنده
    def __init__(self , name , n_id , phone , address = None , email = None):
        self.name = name
        self.n_id = n_id
        self.phone = phone
        self.address = address
        self.email =email

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

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        if not isinstance(new_phone, int):
            raise TypeError("Phone id must be a integer")
        self.__phone = new_phone

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        if not isinstance(new_address, str):
            raise TypeError("Address must be a string")
        self.__address = new_address

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if not isinstance(new_email, str):
            raise TypeError("Email must be a string")
        self.__email = new_email