import fun
import account_handler
import details
while 1:

    n = fun.initial_input()
    if n == 1:
        account_no = fun.account_no(' ')
        pin = fun.pin(' ')
        account = account_handler.Accounts(account_no, pin)
        if account.check_account():
            user_input = fun.existing_user_input()
            if user_input == 1:
                account.check_balance()
            elif user_input == 2:
                amount = fun.amount('send')
                recipient = (input('Enter recipient acc no\t'))
                account.send_money(amount, recipient)
            elif user_input == 3:
                amount = fun.amount('withdrawn')
                account.withdraw(amount)
            elif user_input == 4:
                amount = fun.amount('added')
                account.add_money(amount)
            else:
                print('Invalid Input')
        else:
            print('Invalid account number or password')
    if n == 2:
        acc = fun.account_no('new ')
        if details.existing_account(acc):
            print('Account already exists')
        else:
            pin = fun.pin('new ')
            amt = fun.amount('added')
            new_account = account_handler.Accounts(acc, pin)
            new_account.add_account(amt)
    if n == 3:
        break
