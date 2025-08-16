class BankAccount:
    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance")

    def show_balance(self):
        print("Current Balance:", self.balance)


acc1 = BankAccount("Ankit", "12345", 1000)
acc1.deposit(500)
acc1.withdraw(300)
acc1.show_balance()
