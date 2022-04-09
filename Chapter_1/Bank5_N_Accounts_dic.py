import this


accountList = []


def newaccount(aName, aBalance, aPassword):
    global accountList
    newaccountDict = {'name': aName, 'balance': aBalance, 'password': aPassword}
    accountList.append(newaccountDict)


def show(accountnumber):
    global accountList
    thisAccountDict = accountList[accountnumber]
    print('Account', accountnumber)
    print('     Name', thisAccountDict['name'])
    print('     Balance', thisAccountDict['balance'])
    print('     Password: ', thisAccountDict['password'])
    print()

def getBalance(accountnumber, password):
    global accountList
    thisAccountDict = accountList[accountnumber]
    if password != thisAccountDict[password]:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']


def deposit(accountnumber, amounttodeposit, password):
    global accountList
    thisAccountDict = accountList[accountnumber]

    if amounttodeposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None

    thisAccountDict['balance'] = thisAccountDict['balance'] + amounttodeposit
    return thisAccountDict['balance']
    

def withdraw(accountnumber, amount_to_withdraw, password):
    global accountList
    thisAccountDict = accountList[accountnumber]


    if amount_to_withdraw < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None

    if amount_to_withdraw > thisAccountDict['balance']:
        print('You cannot withdraw more than you have in your account')
        return None

    thisAccountDict['balance']  =  thisAccountDict['balance'] - amount_to_withdraw
    return thisAccountDict['balance']


print("Joe''s account is account number:" ,len(accountList))
newaccount("Joe", 100, 'soup')

print("Mary's account is account number:" ,len(accountList))
newaccount("Mary", 1234, 'nuts')

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
        userpassword = input('Please enter your password: ' )
        the_balance = getBalance(useraccountnumber, userpassword)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    elif action == 'd':
        print('Deposit:')
        useraccount_number= input('Please enter the account number: ')
        useraccount_number = int(useraccount_number)
        userdeposit_amount = input('Please enter amount to deposit: ')
        userdeposit_amount = int(userdeposit_amount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(useraccount_number, userdeposit_amount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 'n':
        print('New Account:')
        username = input('What is your name?')
        user_starting_amount = input('How much money to have to start your account with? ')
        user_starting_amount = int(user_starting_amount)
        userpassword = input('What password would you like to use for this account? ')

        useraccount_number = len(accountList)
        newaccount(username, user_starting_amount, userpassword)
        print('Your new account number is: ', useraccount_number)
        n_accounts = n_accounts + 1

    elif action == 's':
        print('show')
        n_accounts = len(accountList)
        for accountnumber in range(0, n_accounts):
            show(accountnumber)
        show(accountnumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('withdraw')
        useraccountnumber = input('Please enter your account number: ')
        useraccountnumber = int(useraccountnumber)
        user_with_draw_amount =  input('Please enter the amount to withdraw: ')
        user_with_draw_amount = int(user_with_draw_amount)
        userpassword = input('Please enter the password: ')

        new_balance = withdraw(useraccountnumber, user_with_draw_amount, userpassword)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

print('Done')