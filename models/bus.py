from models import carBrand
from models.auto import Auto


class Bus(Auto):

    def __init__(self, color="NoColor", wheel_diameter=0.0, price=0, graduation_year=0, numberOfWindows=0, numberOfStandingPlaces=0, carBrand=carBrand.CarBrand.NISAN):
        super(Bus, self).__init__(color, wheel_diameter, price, graduation_year)
        self.numberOfWindows = numberOfWindows
        self.numberOfStandingPlaces = numberOfStandingPlaces
        self.carBrand = carBrand

    def __str__(self):
        return ('The color of auto is {0}, it wheel_diameter {1} sm, it price {2},'
                + 'graduation_year = {3} year, numberOfWindows = {4}, numberOfStandingPlaces {5},'
                  'carBrand {6} \n').format(
            self.color,
            self.wheel_diameter,
            self.price,
            self.graduation_year,
            self.numberOfWindows,
            self.numberOfStandingPlaces,
            self.carBrand)

    def __repr__(self):
        return self.__str__()

