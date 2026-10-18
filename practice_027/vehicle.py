class Vehicle :
    def __init__(self , name):
        self.name = name

    def __repr__(self):
        return f"Vehicle(name = {self.name})"

    def __benzin(self):
        print("benzin")

    def __hava(self):
        print("hava")

    def __motor(self):
        print("motor")

    def __charkhesh(self):
        print("charkhesh")

    def start(self):
        pass