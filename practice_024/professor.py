#ساخت کلاس استاد یا استفاده از setter و getter

class Professor :
    # متد سازنده
    def __init__(self , name , professor_id , n_id , rank , field , email , phone , salary , degree):
        self.name = name
        self.professor_id = professor_id
        self.n_id = n_id
        self.rank = rank
        self.field = field
        self.email = email
        self.phone = phone
        self.salary = salary
        self.degree = degree

    #متد نمایش رشته ای شی
    def __repr__(self):
        return f"Professor(name={self.name} ,professor_id={self.professor_id} )"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , new_name):
        if not isinstance(new_name , str):
            raise TypeError("Name must be a string")
        self.__name = new_name