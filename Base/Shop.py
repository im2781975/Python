class shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []
    def add(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity' : quantity }
        self.cart.append(product)
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item['price']*item['quantity']
        if total > amount:
            print(f'please provide {total - amount}')
        else:
            amount -= total
            print(f'Here is your remaining {amount}')
    def remove(self, item):
        pass
x = shop('vai')
x.add('A', 12, 15)
x.add('B', 22, 5)
x.add('C', 9, 29)
#print(x.cart)
x.checkout(400)
