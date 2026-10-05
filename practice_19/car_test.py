from car import Car

#PASSED
car1 = Car()
car1.name = "benz"
car1.color ="black"
car1.plate = "1234566"

car1.save()
car1.change_plate()
print(car1)