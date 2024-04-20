class phone:
    menufactured = 'china'
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
    def send(self, phone, sms):
        text = f'Send from {phone}, call me {sms}'
        print(text)
class shop:
    cart =[]
    def __init__(self,buyer):
        self.buyer= buyer
    def add(self,item):
        self.cart.append(item)
a = shop('molla')
a.add('c')
a.add('d')
print(a.cart)

x = phone('A', 'B', 1200)
print(x.owner, x.brand, x.price)
x.send('xphone','Dj')
