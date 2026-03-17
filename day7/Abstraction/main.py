from models.car import Car
from models.bike import Bike

# c = Car("Toyota")
# c.start()

# b = Bike("Honda")
# b.start()

# t = Test()
# t.display()

#polymorphism - same object can take many forms
vehicles = [Car("Toyota"), Bike("Honda")]

for v in vehicles:
    v.start()

