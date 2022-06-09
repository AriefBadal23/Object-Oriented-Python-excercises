from Account import *

class Bank():
    next_account_number = 0
    def __init__(self):
        self.accountdict = {}
        Bank.next_account_number += 1


    def create_account(self, name, start_balance, password):
        oAccount = Account(name, start_balance, password)
        new_account_number = self.next_account_number
        self.accountdict[new_account_number] = oAccount
        return new_account_number


    def open_account(self):
        """ Method  that first asks the user the required details and passing this as parameters to the create_account method """
        print('**Open a account**')
        username = input('What is your name? ')
        start_balance = input('What is the start balance? ')
        start_balance = int(start_balance)
        password = input('What is the password that you want to use? ')
        user_account_number = self.create_account(username, start_balance, password)
        print('Your new account number is:', user_account_number)

    def close_account(self):
        pass



Person1 = Bank()

print(Person1.open_account())

Person2 = Bank()

print(Person2.open_account())


Person3 = Bank()
print(Person3.open_account())