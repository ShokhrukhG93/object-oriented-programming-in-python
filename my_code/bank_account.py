class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print("Name: {}, Balance: {}".format(self.name, self.balance))

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


if __name__ == "__main__":
    a1 = BankAccount()
    a1.set_details("Mike", 200)

    a2 = BankAccount()
    a2.set_details("Tom")

    a1.display()
    a2.display()

    a1.withdraw(100)
    a2.deposit(500)

    a1.display()
    a2.display()
