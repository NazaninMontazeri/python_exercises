#ساخت کلاس درس با استفادهgetterوsetter

class Lesson :
    # متد سازنده
    def __init__(self , code , name , teacher):
        self.code = code
        self.name = name
        self.teacher = teacher

        # متد نمایش رشته ای شی
    def __repr__(self):
        return f"Lesson(code={self.code} , name={self.name} , teacher={self.teacher})"

    @property
    def code(self):
        return  self.__code

    @code.setter
    def code(self , new_code):
        self.__code = new_code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , new_name):
        if not isinstance(new_name , str):
            raise TypeError("Name must  be a string")
        self.__name = new_name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self , new_teacher):
        if not isinstance(new_teacher , str):
            raise TypeError("Teacher must be z string")
        self.__teacher = new_teacher