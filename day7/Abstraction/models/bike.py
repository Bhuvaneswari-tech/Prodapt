from models.base_vehicle import Vehicle

class Bike(Vehicle):
    
    def start(self):
        print(f"{self.brand} bike is starting")

    def bike_type(self):
        print("This is a bike")