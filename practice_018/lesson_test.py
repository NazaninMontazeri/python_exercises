from lesson import Lesson

#passed
lesson1 = Lesson()
lesson1.code = "123456"
lesson1.name = "eeerrrr"
lesson1.teacher = "ahmad"

lesson1.save()
lesson1.edit()
print(lesson1)