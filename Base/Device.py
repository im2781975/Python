class Device:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    def run(self):
        return f'running {self.brand} '
class laptop:
    def __init__(self,memory,ssd):
        self.memory = memory
        self.ssd = ssd
        
    def practice(self):
        pass
class phone(Device):
    def __init__(self, brand, price, color, origin, duality):
        self.duality = duality
        super(). __init__(brand, price,color,origin)
    def call(self, num, sms):
        return f'sending {self.sms} to {self.num} '
    def __repr__(self)->str:
        return f'phone: {self.brand} {self.price} {self.duality} '
        
class camera:
    def __init__(self,pixel):
        self.pixel= pixel
    def change_lens(self):
        pass
x =phone('iphone', 12000, 'silver', 'chine', 'true')
print(x)
print(x.brand)
