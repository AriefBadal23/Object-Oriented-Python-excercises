# Person example using direct access

from Person import *

oPerson1 = Person('Joe Schmoe', 9000)
oPerson2 = Person('Jane Smith', 9900)


# Get the values of the salary variable directly
print(oPerson1.salary)
print(oPerson2.salary)


# Change the salary variable directly
oPerson1.salary = 100000
oPerson1.salary = 110000



# Get the updated salaries and print again
print(oPerson1.salary)
print(oPerson2.salary)

