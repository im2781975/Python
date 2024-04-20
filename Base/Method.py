class phone:
    brand = 'xphone'
    price = 2200
    color = 'blue'
    feature = ['camera', 'speaker', 'hammer']
    def call(self):
        print("calling")
    def send(self,phone, sms):
        text = f'send message to {phone} & message is {sms}'
        return text
class calculator:
    def add(self, a, b):
        return a+b
    def deduct(self, a, b):
        if a >= b:
            return a - b
        else:
            return b - a
    def mult(self, a, b):
        return a * b
    def div(self, a, b):
        return a/b
x = phone()
print(x.brand, x.price, x.color, x.feature)
x.call()
result = x.send(23456, 'mollavai')
print(result)
