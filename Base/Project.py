class bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_= 100
        self.max_= 100000
    def get(self):
        return self.balance
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'After deposite amount is {self.get()}')
    def withdraw(self, amount):
        if amount > self.min_ and amount < self.max_:
            self.balance -= amount
            print(f'Withdrawal amount is {amount}')
            print(f'current balance is {self.balance}')
        else:
            print(f'please write correct amount')
x = bank(15000)
x.withdraw(1200)
x.deposite(2700)
