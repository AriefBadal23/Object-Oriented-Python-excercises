class Account():
    """ Account class for the Bank system to do basic bank account operations"""
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, password, deposit_amount):
        if password != self.password:
            print('Wrong password please enter you password again')
        else:
            self.balance = self.balance + deposit_amount
            print (f'New balance after deposit: {self.balance}')
    
    def withdraw(self, password, withdraw_amount):
        if password != self.password:
            print('Wrong password please enter you password again')
        else:
            self.balance = self.balance - withdraw_amount
            print (f'your current balance is: {self.balance}')


    def get_balance(self, password):
        if password != self.password:
            print('Wrong password please enter you password again')
        else:
            print (f'Hi {self.name}, your current balance is: {self.balance}')


    # Only for debugging/testing purposes
    def show(self):
        print (f'Your name is {self.name}, password {self.password} and balance {self.balance}')




# Account1 = Account('Arief',40000, '1234')
# Account1.deposit('1234', 40)