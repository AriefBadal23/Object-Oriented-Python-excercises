# Main program for controlling a Bank made up for Accounts

from Bank import *
# Info about the bank itself
oBank = Bank('9-5','123 Main Street, Anytown, USA', '(650) 555-1212')

# Main code

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0] # grab the first letter
    print()

    try:
        if action == 'b':
            oBank.balance()

        elif action == 'c':
            oBank.close_Account()
        
        elif action == 'd':
            oBank.deposit()

        elif action == 'i':
            oBank.get_info()
        
        elif action == 'o':
            oBank.open_Account()
        
        elif action == 'q':
            break
        elif action == 's':
            oBank.show()
        
        elif action == 'w':
            oBank.withdraw()

    
    except AbortTransaction as error:
        # Print out the text of the error message
        print(error)