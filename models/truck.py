from models import motor
from models.auto import Auto


class Truck(Auto):

    def __init__(self, color="NoColor", wheel_diameter=0.0, price=0, graduation_year=0, weight=0,
                 numberOfWheels=0, motor=motor.Motor.DIESEL):
        super(Truck, self).__init__(color, wheel_diameter, price, graduation_year)
        self.motor = motor
        self.numberOfWheels = numberOfWheels
        self.weight = weight

    def __str__(self):
        return ('The color of auto is {0}, it wheel_diameter {1} sm, it price {2},'
                + 'graduation_year = {3} year, numberOfWindows = '
                + '{4}, numberOfStandingPlaces {5}, carBrand {6}\n').format(
            self.color,
            self.wheel_diameter,
            self.price,
            self.graduation_year,
            self.weight,
            self.numberOfWheels,
            self.motor)

    def __repr__(self):
        return self.__str__()
