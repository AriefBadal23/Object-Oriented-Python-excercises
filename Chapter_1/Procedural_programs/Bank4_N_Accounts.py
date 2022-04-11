accountnameList = []
accountbalanceList = []
accountpasswordList = []

def newaccount(name, balance, password):
    global accountnameList, accountbalanceList, accountpasswordList
    accountnameList.append(name)
    accountbalanceList.append(balance)
    accountpasswordList.append(password)


def show(accountnumber):
    global accountnameList, accountbalanceList, accountpasswordList
    print('Account', accountnumber)
    print('     Name', accountnameList[accountnumber])
    print('     Balance', accountbalanceList[accountnumber])
    print('     Password: ', accountpasswordList[accountnumber])
    print()

def getBalance(accountnumber, password):
    global accountnameList, accountbalanceList, accountpasswordList

    if password != accountpasswordList[accountnumber]:
        print('Incorrect password')
        return None
    return accountbalanceList[accountnumber]


def deposit(accountnumber, amounttodeposit, password):
    global accountnameList, accountbalanceList, accountpasswordList

    if amounttodeposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != accountpasswordList[accountnumber]:
        print('Incorrect password')
        return None

    accountbalanceList[accountnumber] = accountbalanceList[accountnumber] + amounttodeposit
    return accountbalanceList[accountnumber]
    

def withdraw(accountnumber, amount_to_withdraw, password):
    global accountnameList, accountbalanceList, accountpasswordList

    if amount_to_withdraw < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != accountpasswordList[accountnumber]:
        print('Incorrect password')
        return None

    if amount_to_withdraw > accountbalanceList[accountnumber]:
        print('You cannot withdraw more than you have in your account')
        return None

    accountbalanceList[accountnumber]  =  accountbalanceList[accountnumber] - amount_to_withdraw
    return accountbalanceList[accountnumber]


print("Joe''s account is account number:" ,len(accountnameList))
newaccount("Joe", 100, "soup")

print("Mary's account is account number:" ,len(accountnameList))
newaccount("Mary", 1234, "nuts")

while True:
    print()
    print('Type b to get the balance')
    print('Type d to make a deposit')
    print('Type n to create a new account')
    print('Type w to make a withdrawal')
    print('Type s to show all accounts')
    print('Type q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        useraccountnumber = input('Please enter your account number: ')
        useraccountnumber = int(useraccountnumber)
        userpasword = input('Please enter your password: ' )
        the_balance = getBalance(useraccountnumber, userpasword)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    elif action == 'd':
        print('Deposit:')
        useraccount_number= input('Please enter the account number: ')
        useraccountnumber = int(useraccountnumber)
        userdeposit_amount = input('Please enter amount to deposit: ')
        userdeposit_amount = int(userdeposit_amount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(useraccountnumber, userdeposit_amount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 'n':
        print('New Account:')
        username = input('What is your name?')
        user_starting_amount = input('How much money to have to start your account with? ')
        user_starting_amount = int(user_starting_amount)
        userpasword = input('What password would you like to use for this account? ')

        newaccount(n_accounts, username, user_starting_amount, userpasword)
        print('Your new account number is:', n_accounts)
        n_accounts = n_accounts + 1

    elif action == 's':
        print('show')
        show()

    elif action == 'q':
        break

    elif action == 'w':
        print('withdraw')
        useraccountnumber = input('Please enter your account number: ')
        useraccountnumber = int(useraccountnumber)
        user_with_draw_amount =  input('Please enter the amount to withdraw: ')
        user_with_draw_amount = int(user_with_draw_amount)
        userpasword = input('Please enter the password: ')

        new_balance = withdraw(useraccountnumber, user_with_draw_amount, userpasword)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

print('Done')