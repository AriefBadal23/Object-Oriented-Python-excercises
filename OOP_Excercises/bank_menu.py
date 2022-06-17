from Bank import *

oBank = Bank()

person1 = oBank
person1.create_account('Arief', 100000, 'Password')

person2 = oBank
person2.create_account('Jordan', 200000, 'Password')


while True:
    print('*** Main Menu ***')
    print('Choose option: \
            \n 1.Open account \
            \n 2.Show balance \
            \n 3.Deposit \
            \n 4.Withdraw \
            \n 5.Close account\
            ')

    user_input = input('Make a choice: ')
    user_input = user_input[0].lower()

    if user_input == 'o':
        oBank.open_account()

    # show the balance of the user
    elif user_input == 'b':
        oBank.show_balance()

    elif user_input == 'd':
        oBank.desposit()
        
    elif user_input == 'w':
        oBank.withdraw()

    elif user_input == 'c':
        oBank.close_account()

