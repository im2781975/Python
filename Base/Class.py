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
    class_cart =[]
    def __init__(self,buyer):
        self.buyer= buyer
        self.init_cart = []
    def add(self,item):
        self.class_cart.append(item)
        self.init_cart.append(item)
a = shop('molla')
a.add('c')
a.add('d')
b = shop('vai')
b.add('e')
b.add('f')
c = shop('Aslam')
c.add('g')
c.add('h')
#class attribute will be saved all info but init attribute will be saved specific info
print(a.class_cart)
print(a.init_cart)
print(b.init_cart)
print(c.init_cart)
x = phone('A', 'B', 1200)
print(x.owner, x.brand, x.price)
x.send('xphone','Dj')
