from models import volumeMotor
from models import motor
from models import carBrand
from models.auto import Auto
from models.bus import Bus
from models.car import Car
from models.truck import Truck


class AutoManager:

    def __init__(self, auto_list):
        self.auto_list = auto_list

    def sort_by_price(self, reverse):
        return sorted(self.auto_list, key=lambda auto: auto.price, reverse=reverse)

    def sort_by_color(self, reverse):
        return sorted(self.auto_list, key=lambda auto: auto.color, reverse=reverse)

    def find_graduation_year(self, graduation_year):
        return list(filter(lambda auto: auto.graduation_year == graduation_year, self.auto_list))

    def find_wheel_diameter(self, wheel_diameter):
        return list(filter(lambda auto: auto.wheel_diameter == wheel_diameter, self.auto_list))


car3 = Car("Green", 2.1, 20000, 2017, 7, 1.4, volumeMotor=volumeMotor.VolumeMotor.One)
car4 = Car("Red", 2.1, 20000, 2014, 7, 1.4, volumeMotor=volumeMotor.VolumeMotor.Two)
car1 = Bus("Blue", 3.4, 440000, 2011, 5, 3, carBrand=carBrand.CarBrand.NISAN)
car2 = Bus("Black", 3.2, 60000, 1999, 5, 4, carBrand=carBrand.CarBrand.BMW)
car5 = Truck("Yellow", 2.8, 11111, 1999, 5, 3, motor=motor.Motor.DIESEL)
car6 = Truck("Purple", 2.2, 11112, 2000, 2, 4, motor=motor.Motor.GASOLINE)

goods = [car1, car2, car3, car4, car5, car6]
manager = AutoManager(goods)
print(manager.sort_by_price(False))
print("\n")
print(manager.sort_by_color(True))
print("\n")
print(manager.find_graduation_year(1999))
