class Auto:

    def __init__(self, color="NoColor", wheel_diameter=0.0, price=0, graduation_year=0):
        self.color = color
        self.wheel_diameter = wheel_diameter
        self.price = price
        self.graduation_year = graduation_year

    def __str__(self):
        return ('The item is called {0}, it wheel_diameter {1} sm, it price {2},'
                + 'graduation_year = {3} year \n').format(
            self.color,
            self.wheel_diameter,
            self.price,
            self.graduation_year)

    def __repr__(self):
        return self.__str__()
