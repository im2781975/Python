class Product:
    def __init__(self, name, price, quantity):
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity
class Store:
    def __init__(self):
        self.__products_price = {}
        self.__products_quantity = {}
    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.__products_price[product.product_name] = product.product_price
        self.__products_quantity[product.product_name] = product.product_quantity
    def buy_product(self, name, quantity):
        if name in self.__products_price:
            if self.__products_quantity[name] >= quantity:
                self.__products_quantity[name] -= quantity
                
        else:
            print("Not Found")
    @property
    def show(self):
        print(self.__products_price)
        print(self.__products_quantity)
class Shop(Store):
    def __init__(self, name):
        self.shop_name = name
        super().__init__()
x = Shop("xyz")
x.add_product("abc", 400, 15)
x.add_product("bcd", 200, 20)
x.show
x.buy_product("abc", 2)
x.show
