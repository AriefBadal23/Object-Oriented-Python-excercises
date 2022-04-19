# Bank that manages a dictionary of Account objects
from Account import *

class Bank():
    def __init__(self):
        self.accountsDict = {}
        self.next_account_number = 0

    def createAccount(self, name, starting_amount, password):
        oAccount = Account(name, starting_amount, password)
        new_account_number = self.next_account_number
        self.accountsDict[new_account_number] = oAccount
        # Increment to prepare for next account to be created
        self.next_account_number = self.next_account_number + 1
        return new_account_number


    def openAccount(self):
        print('*** Open Account ***')
        user_name = input('What is the name for the new user account?')
        user_starting_amount = input('What is the starting balance for this account?')
        user_starting_amount = int(user_starting_amount)
        user_password = input('What is the password you want to use for this account?')
        user_account_number = self.createAccount(user_name, user_starting_amount, user_password)
        print('Your new account number is:', user_account_number)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        account_number = input('What is your account number?')
        account_number = int(account_number)
        user_password = input('What is you password?')
        oAccount = self.accountsDict[user_password]
        the_balance = oAccount.getBalance(user_password)
        if the_balance is not None:
            print('You had', the_balance, 'In your account, which is being returned to you')

        # Remove user's account from the dictionary of accounts 
        del self.accountsDict[account_number]
        print('Your account is now closed')

    def balance(self):
        print('*** Get Balance ***')
        account_number = input('Please enter your account number: ')
        account_number = int(account_number)
        user_account_password = input('Please enter the password: ')
        oAccount = self.accountsDict[account_number]
        the_balance = oAccount.get_balance(user_account_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    def deposit(self):
        print('*** Deposit ***')
        account_number = input('Please enter your account number: ')
        account_number = int(account_number)
        deposit_amount = input('Please enter amount to deposit: ')
        deposit_amount = int(deposit_amount)
        user_account_password = input('Please enter your password: ')
        oAccount = self.accountsDict[account_number]
        the_balance = oAccount.deposit(deposit_amount, user_account_password)
        if the_balance is not None:
            print('Your new balance is: ', the_balance)


    def show(self):
        print('*** Show ***')
        for user_account_number in self.accountsDict:
            OAccount = self.accountsDict[user_account_number]
            print('  Account:', user_account_number)
            OAccount.show()


    def withdraw(self):
        print('*** Withdraw ***')
        user_account_number = input('Please enter your account number:')
        user_account_number = int(user_account_number)
        user_amount = input('Please enter the amount to withdraw: ')
        user_amount = int(user_amount)
        user_account_password = input('Please enter the password: ')
        oAccount = self.accountsDict[user_account_number]
        the_balannce = oAccount.withdraw(user_amount, user_account_password)
        if the_balannce is not None:
            print('Withdrew:', user_amount)
            print('Your new balance is:', the_balannce)











