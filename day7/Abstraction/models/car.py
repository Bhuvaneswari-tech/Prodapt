
from models.base_vehicle import Vehicle

class Car(Vehicle):
    
    def start(self):
        print(f"{self.brand} car is starting")

    def car_type(self):
        print("This is a car")
    