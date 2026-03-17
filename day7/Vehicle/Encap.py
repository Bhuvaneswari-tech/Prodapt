class Vehicle:    
    def __init__(self, brand, speed):
        self.brand = brand        # public variable
        self.__speed = speed      # private variable
    
    # def set_speed(self, speed):
    #     self.__speed = speed
    
    def get_speed(self):
        return self.__speed
    
# Example usage
car = Vehicle("Toyota", 120)
print(car.brand)          # Output: Toyota
#print(car.__speed)
print(car.get_speed())    # Output: 120 