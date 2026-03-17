from Car import Car
from Bike import Bike

c = Car("Toyota")
print(c.brand)
c.start()
c.car_type()
print("------------------------------- ")
print("Bike details")
#Bike details
b = Bike("Honda")
print(b.brand)
b.start()
b.bike_type()