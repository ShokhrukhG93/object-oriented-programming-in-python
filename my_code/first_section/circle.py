class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius should be positive")

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    def area(self):
        return 3.14 * self._radius * self._radius


if __name__ == "__main__":
    c1 = Circle(7)
    print(c1.radius, c1.diameter, c1.circumference, c1.area())
    c1.radius = -7
    print(c1.radius, c1.diameter, c1.circumference, c1.area())
