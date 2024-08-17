class Vehicle:
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, Speed):
        self.mode=""
        self.speed = Speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine = enginetype

    def drive(self, speed):
        super().drive


class Motorcycle(Vehicle):
    def __init__(self, enginetype, has_sidecar=False):
        super().__init__("Motorcycle")
        self.wheels = 3 if has_sidecar else 2  
        self.doors = 0
        self.engine = enginetype

car1 = Car("Gas")
car2 = Car("Electric")
mc1 = Motorcycle("Gas", True)  

print(mc1.wheels)  
print(car1.engine)
print(car2.engine)
