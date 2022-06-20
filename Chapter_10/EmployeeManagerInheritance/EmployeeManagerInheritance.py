# Employee Manager inheritance
# 
# Define the Employee class, which we will use as a base class

class Employee():
    def __init__(self, name, title, rate_per_hour=None):
        self.name = name
        self.title = title
        if rate_per_hour is not None:
            rate_per_hour = float(rate_per_hour)
        self.rate_per_hour = rate_per_hour


    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def pay_per_year(self):
        # 52 weeks * 5 days a weel * 8 hours per day
        pay = 52 * 5 * 8 * self.rate_per_hour
        return pay

class Manager(Employee):
    def __init__(self, name, title, salary, reports_list=None):
        self.salary = float(salary)
        if reports_list is None:
            reports_list = []
        self.report_list = reports_list
        super().__init__(name, title)

    def get_reports(self):
        return self.report_list

    def pay_per_year(self, give_bonus=False):
        pay= self.salary
        if give_bonus:
            pay= pay + (10 * self.salary) # add a bonus of 10%
            print(self.name, 'gets a bonus for good work')
            return pay


# create objects
oEmployee1 = Employee('Joe Schmoe', 'Pizza Maker', 16)
oEmployee2 = Employee('Chris Smith', 'Cashier', 14)
oManager = Manager('Sue Jones', 'Pizza Restaurant Manager', 5500, [oEmployee1, oEmployee2])

# Call methods of the Employee objects
print('Employee name: ', oEmployee1.get_name())
print('Employee salary: ', '{:,.2f}'.format(oEmployee1.pay_per_year()))
print('Employee name: ', oEmployee2.get_name())
print('Employee salary: ', '{:,.2f}'.format(oEmployee2.pay_per_year()))
print()

# Call the methods of the Manager object
manager_name = oManager.get_name()
print('Manager name:', manager_name)

# Give the manager a bonus
print('Manager salary: ', '{:,.2f}'.format(oManager.pay_per_year(True)))
print(manager_name, '(' + oManager.get_title() + ')', 'direct reports:')
reports_list = oManager.get_reports()
for oEmployee in reports_list:
    print(' ', oEmployee.get_name(),
    '(' + oEmployee.get_title() + ')')

