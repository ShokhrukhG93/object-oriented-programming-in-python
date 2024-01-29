class Employee:
    allowed_domains = {'yahoo.com', 'outlook.com', 'gmail.com'}
    domains = set()

    def __init__(self, name, email):
        self.name = name
        self._email = email
        domain = email[email.index('@')+1:]
        Employee.domains.add(domain)

    def display(self):
        print(self.name, self.email)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        domain = new_email[new_email.index('@')+1:]
        if domain in Employee.allowed_domains:
            self._email = new_email
        else:
            raise RuntimeError(f'Domain {new_email} is not allowed')


if __name__ == "__main__":
    e1 = Employee('John', 'john@gmail.com')
    e2 = Employee('Jack', 'jack@yahoo.com')
    e3 = Employee('Jill', 'jill@outlook.com')
    e4 = Employee('Ted', 'ted@yahoo.com')
    e5 = Employee('Tim', 'tim@gmail.com')
    e6 = Employee('Mike', 'mike@yahoo.com')

    employees = [e1, e2, e3, e4, e5, e6]

    for employee in employees:
        employee.display()

    print(Employee.allowed_domains)

    e4.email = 'ted@ymail.com'
    e4.display()

    e3.email = 'jill@gmail.com'
    e3.display()
