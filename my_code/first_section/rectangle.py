class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    @property
    def diagonal(self):
        return (self.length*self.length + self.breadth*self.breadth)**0.5

    @property
    def area(self):
        return self.length * self.breadth

    @property
    def perimeter(self):
        return 2 * (self.length + self.breadth)



if __name__ == "__main__":
    r = Rectangle(2, 5)

    print(r.diagonal, r.area, r.perimeter, sep='\n')
    r.breadth = 10
    print(r.diagonal, r.area, r.perimeter, sep='\n')
