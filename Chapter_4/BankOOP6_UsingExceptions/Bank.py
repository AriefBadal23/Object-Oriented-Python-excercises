# Bank that manages a dictionary of Account objects
from Account import *


class Bank:
    """The initiation method which saves all relevant information in instance variables"""

    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.next_account_number = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def ask_for_valid_account_number(self):
        """
        Asks the user for a valid account number with the type int
        If its not a integer it will give an exception
        """
        accountNumber = input("What is your account number? ")
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction("The account number must be an integer")
        # Checks if the account number is in the dictionary with all the accounts
        if accountNumber not in self.accountsDict:
            raise AbortTransaction("There is no account " + str(accountNumber))
        return accountNumber

    def get_users_account(self):
        """Retrieves the accountnumber of the user"""
        account_number = self.ask_for_valid_account_number()
        oAccount = self.accountsDict[account_number]
        self.ask_for_valid_password(oAccount)
        return oAccount

    def ask_for_valid_password(self, oAccount):
        """Ask the user for a valid password"""
        password = input("Please enter your password: ")
        oAccount.checkPasswordMatch(password)

    def create_Account(self, name, starting_amount, password):
        """Method to create a new account for a user"""
        oAccount = Account(name, starting_amount, password)
        new_account_number = self.next_account_number
        self.accountsDict[new_account_number] = oAccount
        # Increment to prepare for next account to be created
        self.next_account_number = self.next_account_number + 1
        return new_account_number

    def open_Account(self):
        """Method to open a account which invokes the create_account method"""
        print("*** Open Account ***")
        user_name = input("What is your name? ")
        user_starting_amount = input("How much money to start your account ?")
        user_password = input("What password would you like to use for this account? ")
        user_account_number = self.create_Account(
            user_name, user_starting_amount, user_password
        )
        print("Your new account number is:", user_account_number)

    def close_Account(self):
        """Method to close a specific account using the acocunt number"""
        print("*** Close Account ***")
        user_account_number = self.ask_for_valid_account_number()
        oAccount = self.accountsDict[user_account_number]
        self.ask_for_valid_password(oAccount)
        the_balance = oAccount.getBalance()
        print("You had", the_balance, "in your account, which is being returned to you.")
        del self.accountsDict[user_account_number]
        print("Ýour account is now closed")

    def balance(self):
        """Outputs the account balance"""
        print("*** Get Balance ***")
        oAccount = self.get_users_account
        theBalance = oAccount.getBalance()
        print("Your balance is:", theBalance)

    def deposit(self):
        """A method to deposit an amount to the bank account"""
        print("*** Deposit ***")
        oAccount = self.get_users_account()
        deposit_amount = input("Please enter amount to deposit: ")
        the_balance = oAccount.deposit(deposit_amount)
        print("Deposited:", deposit_amount)
        print("Your new balance is:", the_balance)

    def withdraw(self):
        """A method to withdraw an amount of the bank account"""
        print("*** Withdraw ***")
        oAccount = self.get_users_account()
        user_amount = input("Please enter the amount to withdraw: ")
        the_balance = oAccount.withdraw(user_amount)
        print("Withdrew: ", user_amount)
        print("Your new balance is:", the_balance)


    def get_info(self):
        """Get information about a bank acount"""
        print("Hours: ", self.hours)
        print("Address: ", self.address)
        print("Phone:", self.phone)
        print("We currently have", len(self.accountsDict), "account(s) open.")


    # Special method for Bank admin only
    def show(self):
        print("*** Show ***")
        print("(This would typically require an admin password)")
        for user_account_number in self.accountsDict:
            oAccount = self.accountsDict[user_account_number]
            print("Account", user_account_number)
            oAccount.show()
            print()
