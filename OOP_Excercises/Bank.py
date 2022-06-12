from stringprep import in_table_a1
from Account import *

class Bank():
    def __init__(self):
        self.accountdict = {}
        self.next_account_number = 0


    def create_account(self, name, start_balance, password):
        """ Method to create a new Bank account """
        oAccount = Account(name, start_balance, password)
        new_account_number = self.next_account_number
        self.accountdict[new_account_number] = oAccount
        self.next_account_number = self.next_account_number + 1
        return new_account_number

      
    def open_account(self):
        """ Method to open a specific Bank account """
        print('**Open a account**')
        username = input('What is your name? ')
        start_balance = input('What is the start balance? ')
        start_balance = int(start_balance)
        password = input('What is the password that you want to use? ')
        user_account_number = self.create_account(username, start_balance, password)
        print('Your new account number is:', user_account_number)

    def close_account(self):
        """ Method to close a specific Bank account """
        account_number = input('What is the account number? ')
        print('The remaining balance will be returned')
        del self.accountdict[int(account_number)]



    def show_balance(self):
        """ Method to show the balance of a specif Bank account  """
        # ask account_number & ask password
        pass
        

