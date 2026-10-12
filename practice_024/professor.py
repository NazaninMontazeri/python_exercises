#ساخت کلاس استاد یا استفاده از setter و getter

class Professor :
    # متد سازنده
    def __init__(self , name , professor_id , n_id , rank , field , email , phone , salary):
        self.name = name
        self.professor_id = professor_id
        self.n_id = n_id
        self.rank = rank
        self.field = field
        self.email = email
        self.phone = phone
        self.salary = salary

    #متد نمایش رشته ای شی
    def __repr__(self):
        return f"Professor(name={self.name} ,professor_id={self.professor_id} )"
