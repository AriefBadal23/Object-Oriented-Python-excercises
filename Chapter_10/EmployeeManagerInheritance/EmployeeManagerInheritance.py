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


        