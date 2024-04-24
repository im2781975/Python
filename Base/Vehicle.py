class vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f'{self.name} {self.price}'
    def move(self):
        pass
class bus(vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)
class truck(vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)
class PickUpTruck(truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)
class AcBus(bus):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)
    def __repr__(self)->str:
        print(f'{self.seat}')
        return super().__repr__()
        
x = AcBus('abc', 500000, 22, 16)
print(x)
