# person class


class Person():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Allows the caller to retrieve the salary
    def get_salary(self):
        return self.salary

    # Allow the caller to set a new salary
    def set_salary(self, salary):
        self.salary = salary