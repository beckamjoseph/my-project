class Account:
    account_name="OLUWASEYI AARON JOSEPH"
    account_number="2405970788"
    account_balance=2000
    def __init__(self):
        self.account_name
        self.account_number
        self.account_balance
    def deposit(self, amount):
        self.account_balance=self.account_balance+amount
        return "Thank you for doing buisness with us"
    def withdraw(self, amount):
        self.account_balance=self.account_balance-amount
        return "Thank you for taking your money"