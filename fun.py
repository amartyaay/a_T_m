def initial_input():
    n = int(input('''
1 -> LogIn
2 -> SignUp
3 -> Quit
'''))
    return n


def existing_user_input():
    n = int(input('''
Enter 1 to display balance.
Enter 2 to send money.
Enter 3 to withdraw money.
Enter 4 to add money.
Enter 5 to LogOut.
'''))
    return n


def account_no(s):
    n = input(f'Enter {s}account number\t')
    return n


def pin(s):
    n = input(f'Enter {s}pin\t')
    return n


def amount(s):
    n = input(f'Enter amount to be {s}\t')
    return n
