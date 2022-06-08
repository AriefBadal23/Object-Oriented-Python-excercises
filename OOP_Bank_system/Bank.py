from Account import *

class Bank():
    def __init__(self):
        self.accountdict = {}
        self.next_account_number = 0


    def create_account(self, name, start_balance, password):
        oAccount = Account(name, start_balance, password)
        new_account_number = self.next_account_number
        self.accountdict[new_account_number] = oAccount
        self.next_account_number = self.next_account_number + 1
        return new_account_number   


    def open_account(self):
        """ Method  that first asks the user the required details and passing this as parameters to the create_account method """
        print('**Open a account**')
        username = input('What is your name? ')
        start_balance = input('What is the start balance? ')
        password = input('What is the password that you want to use? ')
        user_account_number = self.create_account(username, start_balance, password)
        print(f'Your new account number is:{user_account_number}')

    def close_account(self):
        pass



p = Bank()
print(p.create_account('Arief', 400, 'password123'))

p2 = Bank()
p2.create_account('John', 2000, 'password123')



        


    