from Person import *

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('jane Smith', 99000)


# Get the salaries using getter and print
print(oPerson1.get_salary())
print(oPerson2.get_salary())


# Change the salaries using setter
oPerson1.set_salary(100000)
oPerson2.set_salary(111111)

# Get the salaries and print again
print(oPerson1.get_salary())
print(oPerson2.get_salary())