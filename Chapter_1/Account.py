from tkinter.messagebox import NO


class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amountToDeposit < 0:
            print('Your cannot deposit a negative amount')
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    
    def withdraw(self, amountTowithdraw, password):
        if password != self.password:
            print('Inccorect password for this account')
            return None

        if amountTowithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None

        self.balance = self.balance - amountTowithdraw

    
    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        return self.balance


    def show(self):
        print(' Name:', self.name)
        print(' Balance:', self.balance)
        print(' Password:', self.password)
        print()
