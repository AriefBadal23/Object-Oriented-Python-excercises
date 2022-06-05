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
            return self.balance
    
    def withdraw(self, password, withdraw_amount):
        if password != self.password:
            print('Wrong password please enter you password again')
        else:
            self.balance = self.balance - withdraw_amount
            return self.balance


    def get_balance(self, password):
        if password != self.password:
            print('Wrong password please enter you password again')
        else:
            return self.balance



    # Only for debugging/testing purposes
    def show(self):
        print (f'Your name is {self.name}, password {self.password} and balance {self.balance}')


        
p = Account('Arief', 2000, 'Kip123')
# p.deposit('Kip123',2000)
# p.withdraw('Kip123',2000)
print(p.get_balance('Kip123'))
p.show()

