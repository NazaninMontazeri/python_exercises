# ساخت کلاس استاد یا استفاده از setter و getter

class Professor:
    # متد سازنده
    def __init__(self, name, professor_id, n_id, rank, field, email, phone, salary, degree):
        self.name = name
        self.professor_id = professor_id
        self.n_id = n_id
        self.rank = rank
        self.field = field
        self.email = email
        self.phone = phone
        self.salary = salary
        self.degree = degree

    # متد نمایش رشته ای شی
    def __repr__(self):
        return f"Professor(name={self.name} ,professor_id={self.professor_id} )"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self.__name = new_name

    @property
    def professor_id(self):
        return self.__professor_id

    @professor_id.setter
    def professor_id(self, new_professor_id):
        if not isinstance(new_professor_id, int):
            raise TypeError("Professor id must be a integer")
        self.__professor_id = new_professor_id

    @property
    def n_id(self):
        return self.__n_id

    @n_id.setter
    def n_id(self, new_n_id):
        if not isinstance(new_n_id, int):
            raise TypeError("N id must be a integer")
        self.__n_id = new_n_id

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, new_rank):
        if not isinstance(new_rank, str):
            raise TypeError("Rank must be a string")
        self.__rank = new_rank

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, new_field):
        if not isinstance(new_field, str):
            raise TypeError("Field must be a string")
        self.__field = new_field

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if not isinstance(new_email, str):
            raise TypeError("Email must be a string")
        self.__email = new_email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        if not isinstance(new_phone, int):
            raise TypeError("Phone id must be a integer")
        self.__phone = new_phone

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, int):
            raise TypeError("Salary id must be a integer")
        self.__salary = new_salary

    @property
    def degree(self):
        return self.__degree

    @degree.setter
    def degree(self, new_degree):
        if not isinstance(new_degree, str):
            raise TypeError("Degree must be a string")
        self.__degree = new_degree
