
def file_handler():
    f = open('dnt_u_dare_tch_it.mf', 'r')
    details = []
    for i in f:
        details.append(i.split(':'))
    f.close()
    return details


def existing_account(acc_no):
    for i in file_handler():
        if int(i[0]) == int(acc_no):
            return 1
    return 0


def pin_check(a, pin):
    for i in file_handler():
        if int(i[0]) == int(a) and int(i[1]) == int(pin):
            # account_file_handler().append(i)
            return 1


def check_balance(a):
    balance = 0
    for i in file_handler():
        if int(i[0]) == int(a):
            # balance += int(i[2][:-1])
            balance = i[2]
    return balance
    # return account_file_handler()[2]


def send(a, p, amount, r):
    crnt_blnce_sender = int(check_balance(a)[:-1])
    if int(amount) > crnt_blnce_sender:
        print('Not enough balance')
    else:
        crnt_blnce_reciever = int(check_balance(r)[:-1])
        r_pin = None
        for i in file_handler():
            if int(i[0]) == int(r):
                r_pin = i[1]
        f = open('dnt_u_dare_tch_it.mf', 'a')
        f.write(a+":"+p+":"+str(crnt_blnce_sender-int(amount))+"\n")
        f.write(r+":"+r_pin+":"+str(crnt_blnce_reciever+int(amount))+"\n")
        f.close()
        print('Money sent successfully')


def add_acc(a, p, amt):
    f = open('dnt_u_dare_tch_it.mf', 'a')
    f.write(a+":"+p+":"+amt+"\n")
    f.close()


def withdraw(a, p, amt):
    crnt_blnce = check_balance(a)
    crnt_blnce = int(crnt_blnce[:-1])
    if int(amt) > crnt_blnce:
        print('Not enough balance')
    else:
        f = open('dnt_u_dare_tch_it.mf', 'a')
        f.write(a+":"+p+":"+str(crnt_blnce-int(amt))+"\n")
        f.close()
        print('Money withdrawn successfully')


def add_money(a, p, amt):
    if int(amt) > 0:
        crnt_blnce = int(check_balance(a)[:-1])
        f = open('dnt_u_dare_tch_it.mf', 'a')
        f.write(a+":"+p+":"+str(crnt_blnce+int(amt))+"\n")
        f.close()
        print('Money added successfully')
    else:
        print('no negative money pls')
