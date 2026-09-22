class BankAccount:

    def __init__(self, account_number, holder, balance):

        self.account_number = account_number
        self.holder = holder
        self.balance = balance
    def display_balance(self):
        print("Balance =", self.balance)
num = int(input("Enter account number: "))
tile = input("Enter account holder name: ")
account=BankAccount(num, tile,"Your Balance is: 50000")
account.display_balance()