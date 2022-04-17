# Test program using accounts
# Version 3 using a dictionary of accounts

# Bring in all the code from the Account class file
from Account import *

accountsDict = {}
next_account_number = 0


# Create two accounts:
oAccount = Account('Joe', 100, 'JoesPassword')
joes_account_number = next_account_number
accountsDict[joes_account_number] = oAccount
print('Account number for Joe is:', joes_account_number)
next_account_number = next_account_number + 1


oAccount = Account('Mary', 1234, 'MarysPassword')
marys_account_number = next_account_number
accountsDict[marys_account_number] = oAccount
print('Account number for Mary is:', marys_account_number)
next_account_number = next_account_number + 1


accountsDict[joes_account_number].show()
accountsDict[marys_account_number].show()
print()


# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
accountsDict[joes_account_number].deposit(50, 'JoesPassword')
accountsDict[marys_account_number].withdraw(345, 'MarysPassword')
accountsDict[marys_account_number].deposit(100, 'MarysPassword')

# Show the accounts
accountsDict[joes_account_number].show()
accountsDict[marys_account_number].show()

# Create another account with information from the user
print()
user_name = input('What is the name for the user account? ')
user_balance = input('What is the starting balance for this account? ')
user_balance = int(user_balance)
user_password = input('What is the password you want to use for this account? ')

# New instance of the Account class
oAccount = Account(user_name,user_balance, user_password)
new_account_number = next_account_number
accountsDict[new_account_number] = oAccount
print('Account number for new account is:', new_account_number)
next_account_number = next_account_number + 1


# Show the newly created user account
accountsDict[new_account_number].show()
user_balance = accountsDict[new_account_number].getbalance(user_password)
print()
print('After depositing 100, user balance is:', user_balance)


# Show the new account
accountsDict[new_account_number].show()
