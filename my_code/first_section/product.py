class Product:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    @property
    def value(self):
        # only get a value
        return self._x

    @value.setter
    def value(self, value):
        # only set a value
        self._x = value

    @value.deleter
    def value(self):
        print("Value deleted")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val

    @y.deleter
    def y(self):
        print("Value of y deleted")


if __name__ == "__main__":
    p = Product(100, 200)

    p.display()

    p.value = 20
    p.y = 30

    p.display()

    del p.value
    del p.y
