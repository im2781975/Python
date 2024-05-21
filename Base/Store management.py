class person:
    id_counter = 100
    def __init__(self, email, password):
        self.email = email
        self.password = password
        #self.user_id = person.id_counter
        #person.id_counter += 1
        self.user_id = person.generate_id()
    @classmethod
    def generate_id(self):
        id = self.id_counter
        self.id_counter += 1
        return id
    def __repr__(self):
        return f"{self.email} {self.user_id}"
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __repr__(self):
        return f"{self.name} {self.price} {self.quantity}"
class store:
    def __init__(self):
        self.total_product = {}
class owner(person):
    def __init__(self, email, password):
        super().__init__(email, password)
class seller(person):
    def __init__(self, email, password):
        super().__init__(email, password)
    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        print(product)
class customer(person):
    def __init__(self, email, password):
        super().__init__(email, password)
s= seller("kepler646@gmail.com", 1234)
m = seller("hakim@gmail.com", 2345)
print(s)
s.add_product("xphone", 120, 24)
m.add_product("yphone", 150, 6)
print(m)
