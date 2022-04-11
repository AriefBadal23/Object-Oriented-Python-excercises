# Without any OOP
# Bank version 1
# A single account


account_name = 'Joe'
account_balance = 100
account_password = 'soup'


while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()


    if action == 'b':
        print('get Balance')
        user_password = input("Please enter the password: ")
        if user_password != account_password:
            print('Incorrect password!')
        else:
            print('Your balance is: ', account_balance)

    elif action == 'd':
        print('Deposit')
        user_deposit_amount = input('Please enter amount to deposit: ')
        user_deposit_amount = int(user_deposit_amount)
        user_password = input('Please enter the password: ')

        if user_deposit_amount < 0:
             print('You cannot deposit a negative amount!')
        
        elif user_password != account_password:
            print('Incorrect password')

        else: #OK
            account_balance = account_balance + user_deposit_amount
            print('Your new balance is:', account_balance)

    elif action == 's':
        print('Show')
        print('       Name', account_name)
        print('       Balance:', account_balance)
        print('       Password:', account_password)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')

        user_with_draw_amount = input('Please enter the amount to withdraw: ')
        user_with_draw_amount = int(user_with_draw_amount)
        userPassword = input('Please enter the password: ')

        if user_with_draw_amount < 0:
            print('You cannot withdraw a negative amount')

        elif userPassword != account_password:
            print('Incorrect password for this account')

        elif user_with_draw_amount > account_balance:
            print('You cannot withdraw more than you have in your account')

        else:  #OK
            account_balance = account_balance - user_with_draw_amount
            print('Your new balance is:', account_balance)

print('Done')



