# Test program using accounts
# Version1, using explicit variables for each Account object

# Bring in all the code from the Account class file
from Account import Account

# Create two accounts
oJoesAccount = Account('Joe', 100, 'JoesPassword')
print('Created an account for Joe')

oMarysAccount = Account('Mary', 1234, 'MarysPassword')
print('Created an account for Mary')


oJoesAccount.show()
oMarysAccount.show()
print()


# Call some methods on the different account
print('Calling method of the two account...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# Show the accounts
oJoesAccount.show()
oMarysAccount.show()

# Create another account with information from the user
print()
userName = input('What is the name for the user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')

# New instance of the Account class
oNewAccount = Account(userName,userBalance, userPassword)

# Show the newly created user account
oNewAccount.show()

# Let's deposit 100 into the new account
oNewAccount.deposit(100, userPassword)
userBalance = oNewAccount.getbalance(userPassword)
print()
print('After depositing 100, users balance is:', userBalance)

# Show the new account
oNewAccount.show()

