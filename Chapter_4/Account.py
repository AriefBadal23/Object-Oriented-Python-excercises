# Account class

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    
    def deposit(self, amount_to_deposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amount_to_deposit < 0:
            print('You cannot deposit a negative amount')
            return None

        self.balance = self.balance + amount_to_deposit
        return self.balance

    
    def withdraw(self, amount_to_withdraw, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amount_to_withdraw < 0:
            print('You cannot withdraw a negative amount')
            return None

        
        if amount_to_withdraw > self.balance:
            print('You cannot withdraw more than you have in your account')
            return None

        self.balance = self.balance - amount_to_withdraw
        return self.balance

    
    def getbalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        return self.balance


    def show(self):
        print('     Name:', self.name)
        print('     Balance:', self.balance)
        print('     Password:', self.password)
        print()


