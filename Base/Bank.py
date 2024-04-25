class bank:
    def __init__(self, name, initial):
        self.name = name 
        #public
        self._branch = 'Banani'
        #protected
        self.__balance = initial
        #private
    def deposite(self, amount):
        self.__balance +=amount
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance-=amount
            return amount
        else:
            return f'Insufficient Balance'
    def get(self):
        return self.__balance
xyz = bank('abc', 5000)
xyz.deposite(1000)
xyz.withdraw(500)
print(xyz.get())
#print(dir(xyz))
