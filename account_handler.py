import details


class Accounts:
    def __init__(self, a, p):
        super().__init__()
        self.account_no = a
        self.pin = p

    def check_account(self):
        return details.pin_check(self.account_no, self.pin)

    def add_account(self, amount):
        if details.existing_account(self.account_no):
            print('account already exsists')
        else:
            details.add_acc(self.account_no, self.pin, amount)

    def check_balance(self):
        print(details.check_balance(self.account_no))

    def withdraw(self, amount):
        details.withdraw(self.account_no, self.pin, amount)

    def send_money(self, amount, recipient):
        if details.existing_account(recipient):
            details.send(self.account_no, self.pin, amount, recipient)
        else:
            print("invalid recipient")

    def add_money(self, amt):
        details.add_money(self.account_no, self.pin, amt)
