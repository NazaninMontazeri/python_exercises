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