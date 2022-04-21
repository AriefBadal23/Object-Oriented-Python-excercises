# Account class
# Errors indicated by "raise" statements

# Define a custom exception
class AbortTransaction(Exception):
    "raise this exception to abort a bank transaction"
    pass


class Account():
    def __init__(self, name, balance, password):
        self.name = name
        # Makes sure that the starting balance is valid by calling the validateAmount()
        self.balance = self.validateAmount(balance)
        self.password = password

    
    def validateAmount(self, amount):
        """
         Method which ensures that the starting amount can be converted to a integer.
         If not it will raise an exception. It also checks if the integer is positive. 
        """
        try:
            amount = int(amount)
        except:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount


    def checkPasswordMatch(self, password):
        """ 
        Checks if the password supplied by the user matches the password saved the account.
        If not it will raise an exception.
        """
        if password != self.password:
            raise AbortTransaction('Incorrect password for this account')


    def deposit(self, amount_to_deposit):
        """ 
        Checks if the amount to deposit is an integer and returns the balance of the account
        """
        amount_to_deposit = self.validateAmount(amount_to_deposit)
        self.balance = self.balance + amount_to_deposit
        return self.balance

    def getBalance(self):
        """ Returns the balance of the account """
        return self.balance

    def withdraw(self, amount_to_withdraw):
        """ 
        Checks if the amount to withdraw is more than the actual balance of the account
        If so it will raise an exception.
        """
        amount_to_withdraw = self.validateAmount(amount_to_withdraw)
        if amount_to_withdraw > self.balance:
            raise AbortTransaction('You cannot withdraw more than you have in your account')

        self.balance = self.balance - amount_to_withdraw
        return self.balance


    # Added for debugging
    def show(self):
        print('     Name:', self.name)
        print('     Balance:', self.balance)
        print('     Password:', self.password)


