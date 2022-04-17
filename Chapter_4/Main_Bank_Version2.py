# Test program using accounts
# Version 2, using a list of accounts

# Bring in all the code from the Account class file
from Account import Account
accounts_list = []

# Create two accounts
oAccount = Account('Joe', 100, 'JoesPassword')
accounts_list.append(oAccount)
print("Joe's account number is 0")

oAccount = Account('Mary', 1234, 'MarysPassword')
accounts_list.append(oAccount)
print("Mary's account number is 1")

accounts_list[0].show()
accounts_list[1].show()
print()



# Call some methods on the different account
print('Calling methods of the two accounts...')
accounts_list[0].deposit(50, 'JoesPassword')
accounts_list[1].withdraw(345, 'MarysPassword')
accounts_list[1].deposit(100, 'MarysPassword')

# Show the accounts
accounts_list[0].show()
accounts_list[1].show()

# Create another account with information from the user
print()
user_name = input('What is the name for the user account? ')
user_balance = input('What is the starting balance for this account? ')
user_balance = int(user_balance)
user_password = input('What is the password you want to use for this account? ')

# New instance of the Account class
oAccount = Account(user_name,user_balance, user_password)
accounts_list.append(oAccount) # append to list of accounts


print('Create new account, account number is 2')
# Show the newly created user account
accounts_list[2].show()

# Let's deposit 100 into the new account
accounts_list[2].deposit(100, user_password)
user_balance = accounts_list[2].getbalance(user_password)
print()
print('After depositing 100, users balance is:', user_balance)

# Show the new account
accounts_list[2].show()

