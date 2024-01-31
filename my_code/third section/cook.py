class Mother:
    def cook(self):
        print("Can cook pasta")


class Father:
    def cook(self):
        print("Can cook noodles")


class Daughter(Father, Mother):
    pass


class Son(Mother, Father):
    def cook(self):
        super().cook()
        print("Can cook butter chicken")


if __name__ == "__main__":
    d = Daughter()
    s = Son()

    d.cook()  # Can cook noodles
    print()
    s.cook()  # Can cook pasta, Can cook butter chicken
