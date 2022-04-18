# Test program using accounts
# Version 4 using a dictionary of accounts

# Bring in all the code from the Account class file
from Account import *

accountsDict = {}
next_account_number = 0


# Build some starting accounts for testing
oAccount = Account("Joe", 100, "JoesPassword")
joes_account_number = next_account_number
accountsDict[joes_account_number] = oAccount
print("Account number for Joe is:", joes_account_number)
# increment the account number after assignment
next_account_number = next_account_number + 1


oAccount = Account("Mary", 1234, "MarysPassword")
marys_account_number = next_account_number
accountsDict[marys_account_number] = oAccount
print("Account number for Mary is:", marys_account_number)
next_account_number = next_account_number + 1


while True:
    print()
    print("press b to get the balance")
    print("press d to make a deposit")
    print("press o to open a new account")
    print("press w to make a withdrawal")
    print("press s to show all the accounts")
    print("press q to quit")
    print()

    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0]  # grab the first letter
    print()

    if action == "b":
        print("** Get Balance **")
        user_account_number = input("Please enter your account number ")
        user_account_number = int(user_account_number)
        user_password = input("Please enter your password: ")
        oAccount = accountsDict[user_account_number]
        the_balance = oAccount.getbalance(user_password)
        if the_balance is not None:
            print("Your balance is:", the_balance)

    elif action == "d":
        print("** Deposit **")
        user_account_number = input("Please enter your account number ")
        user_account_number = int(user_account_number)
        user_deposit_amount = input("Please enter the amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_password = input("Please enter your password: ")
        oAccount = accountsDict[user_account_number]
        the_balance = oAccount.deposit(user_deposit_amount,user_password)
        if the_balance is not None:
            print("Your balance is:", the_balance)


    elif action == 'o':
        print("** Open Account **")
        user_name = input('What is the name for the new user account? ')
        user_starting_amount = input('What is the starting balamce for this account? ')
        user_starting_amount = int(user_starting_amount)
        user_password = input('What is the password you want to use for this account? ')
        oAccount = Account(user_name, user_starting_amount, user_password)
        accountsDict[next_account_number] = oAccount
        print('Your new account number is:', next_account_number)
        next_account_number = next_account_number + 1
        print()

    elif action == 's':
        print('Show:')
        for user_account_number in accountsDict:
            oAccount = accountsDict[user_account_number]
            print(' Account Number:' , user_account_number)
            oAccount.show() #userAccountNumber

    elif action == 'q':
        break

    elif action == 'w':
        print('*** Withdraw ***')
        user_account_number = input("Please enter your account number")
        user_account_number = int(user_account_number)
        user_withdrawal_amount = input("Please enter the amount to withdraw: ")
        user_withdrawal_amount = int(user_withdrawal_amount)
        user_password = input("Please enter your password: ")
        oAccount = accountsDict[user_account_number]
        the_balance = oAccount.withdraw(user_withdrawal_amount,user_password)
        if the_balance is not None:
            print("Withdrew:" , user_withdrawal_amount)
            print('Your new balance is:' , the_balance)

    else:
        print('Sorry, that was not a valid action. Please try again.')

print('Done')