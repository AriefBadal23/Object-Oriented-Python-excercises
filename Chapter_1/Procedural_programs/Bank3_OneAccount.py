account0_name = ''
account0_balance = 0
account0_password = ''
account1_name = ''
account1_balance = 0
account1_password = ''
n_accounts = 0



def newaccount(accountnumber, name, balance, password):
    global account0_name, account0_balance, account0_password
    global account1_name, account1_balance, account1_password

    if accountnumber == 0:
        account0_name = name
        account0_balance = balance
        account0_password = password

    if accountnumber == 1:
        account1_name = name
        account1_balance = balance
        account1_password = password


def show():
    global account0_name, account0_balance, account0_password
    global account1_name, account1_balance, account1_password

    if account0_name != '':
        print('Account 0')
        print('     Name', account0_name)
        print('     Balance', account1_balance)
        print('     Password: ', account0_password)

    if account1_name != '':
        print('Account 1')
        print('     Name', account1_name)
        print('     Balance', account1_balance)
        print('     Password: ', account1_password)

def getBalance(accountnumber, password):
    global account0_name, account0_balance, account0_password
    global account1_name, account1_balance, account1_password

    if accountnumber == 0:
        if password != account0_password:
            print('Incorrect password')
            return None
        return account0_balance

    
    if accountnumber == 1:
        if password != account1_password:
            print('Incorrect password')
            return None
        return account1_balance

def deposit(accountnumber, amounttodeposit, password):
    global account0_name, account0_balance, account0_password
    global account1_name, account1_balance, account1_password
    
    if accountnumber == 0:
        if amounttodeposit < 0:
            print('You cannot deposit a negative amount!')
            return None

        if password != account0_password:
            print('Incorrect password')
            return None

        account0_balance = account0_balance + amounttodeposit
        return account0_balance

        
    if accountnumber == 1:
        if amounttodeposit < 0:
            print('You cannot deposit a negative amount!')
            return None

        if password != account1_password:
            print('Incorrect password')
            return None

        account1_balance = account1_balance + amounttodeposit
        return account1_balance

def withdraw(accountnumber, amount_to_withdraw, password):
    global account0_name, account0_balance, account0_password
    global account1_name, account1_balance, account1_password


    if accountnumber == 0:
            if amount_to_withdraw < 0:
                print('You cannot deposit a negative amount!')
                return None

            if password != account0_password:
                print('Incorrect password')
                return None

            if amount_to_withdraw > account0_balance:
                print('You cannot withdraw more than you have in your account')
                return None

            account0_balance = account0_balance + amount_to_withdraw
            return account0_balance

    if accountnumber == 1:
            if amount_to_withdraw < 0:
                print('You cannot deposit a negative amount!')
                return None

            if password != account1_password:
                print('Incorrect password')
                return None

            if amount_to_withdraw > account1_balance:
                print('You cannot withdraw more than you have in your account')
                return None

            account0_balance = account1_balance + amount_to_withdraw
            return account1_balance

# call newaccount function
newaccount(n_accounts,"Joe", 100, 'soup')
n_accounts = 1

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