from models import volumeMotor
from models.auto import Auto


class Car(Auto):

    def __init__(self, color="NoColor", wheel_diameter=0.0, price=0, graduation_year=0, seats=0, loadCapacity=0.0,
                 volumeMotor=volumeMotor.VolumeMotor.One):
        super(Car, self).__init__(color, wheel_diameter, price, graduation_year)
        self.volumeMotor = volumeMotor
        self.loadCapacity = loadCapacity
        self.seats = seats

    def __str__(self):
        return ('The color of auto is {0}, it wheel_diameter {1} sm, it price {2},'
                + 'graduation_year = {3} year, seats = {4}, loadCapacity {5}, '
                + 'volumeMotor {6} \n').format(
            self.color,
            self.wheel_diameter,
            self.price,
            self.graduation_year,
            self.seats,
            self.loadCapacity,
            self.volumeMotor,)

    def __repr__(self):
        return self.__str__()
