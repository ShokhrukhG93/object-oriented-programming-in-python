class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1

    def show(self):
        print(f"{self.nr} / {self.dr}")

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr*other.dr + other.nr*self.dr, self.dr*other.dr)

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x%s == 0 and y%s == 0:
                break
            s -= 1
        return s


if __name__ == "__main__":
    f1 = Fraction(2, 3)
    f1.show()
    f2 = Fraction(2, -3)
    f2.show()
    f3 = Fraction(-5, -6)
    f3.show()
    print("_" * 50)

    f1 = Fraction(2, 3)
    f1.show()
    f2 = Fraction(3, 4)
    f2.show()
    f3 = f1.multiply(f2)
    f3.show()
    f3 = f3.add(f2)
    f3.show()
    f3 = f1.add(5)
    f3.show()
    print("_" * 50)

    f1 = Fraction(2, 3)
    f1.show()
    f2 = Fraction(2, -3)
    f2.show()
    f3 = Fraction(-5, -6)
    f3.show()
    print(Fraction.hcf(-5, -6))
    