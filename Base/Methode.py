class shop:
    cart = [] #static or class attribute
    origin = 'china'
    def __init__(self, name, location):
        self.name ='B Bazar'
        #instance attribute
        self.location = 'Caserta'
    def purches(self, item, price, amount):
        remain = amount - price
        print(f'Buying {item} for price {price} remaining {remain} ')
    @staticmethod
    def multiply(a, b):
        print(a*b)
    @classmethod
    def showoff(self, item):
        print(item)
#shop.purches('a', 4, 2, 2)
a = shop('name', 'location')
a.purches('x', 2, 2)
a.showoff('Lungi')
shop.showoff('Lungi')
shop.multiply(8, 9)
#class method can access without useof instance
#static mathod can't change or pri t class info
