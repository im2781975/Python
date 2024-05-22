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
class Store:
    def __init__(self):
        self.total_product = {}
    def add_product(self, seller_id, product):
        print(seller_id)
        product_Dict = vars(product)
        print(product_Dict)
        if seller_id not in self.total_product:
            self.total_product[seller_id] = []
            seller_info = {}
            seller_info["total_sell_product"] = 0
            seller_info["total_sell_amount"] = 0
            seller_info["total_profit_amount"] = 0
            self.total_product[seller_id].append(seller_info)
        self.total_product[seller_id].append(product_Dict)
class owner(person):
    def __init__(self, email, password):
        super().__init__(email, password)
class seller(person):
    def __init__(self, email, password):
        super().__init__(email, password)
    def add_product(self, store, name, price, quantity):
        product = Product(name, price, quantity)
        store.add_product(self.user_id, product)
class customer(person):
    def __init__(self, email, password):
        self.total_buy_amount = 0
        self.buy_product = 0
        super().__init__(email, password)
    def show_products(self, store):
      #  print(store.total_product[100])
        all_seller_keys = store.total_product.keys()
        for seller_id in all_seller_keys:
            print(seller_id)
            """
            for product in store.total_product[seller_id]:
                print(product["name"], product["price"], product["quantity"]) """
            for index in range(1, len(store.total_product[seller_id])):
                product = store.total_product[seller_id][index]
                print(product["name"], product["price"], product["quantity"])
    def buy_product(self, store, seller_id, product_name, quantity):
        #print(store.total_product[seller_id])
        for index in range(1, len(store.total_product[seller_id])):
            product = store.total_product[seller_id][index]
            if product["name"] == product_name:
                product["quantity"] -= quantity
                self.total_buy_product += quantity
                self.total_buy_amount += product["price"]*quantity
                seller = store.total_product[seller_id][0]
                seller["total_sell_product"]+=quantity
                seller["total_sell_amount"]+=product["price"]*quantity
        
store = Store()
s= seller("kepler646@gmail.com", 1234)
m = seller("hakim@gmail.com", 2345)
print(s)
s.add_product(store, "xphone", 120, 24)
m.add_product(store, "yphone", 150, 6)
print(m)
print(store.total_product)
cust = customer("@gmail.com", 3456)
#print(store.total_product)
cust.buy_product(store,101, "yphone",1)
cust.show_product(store)
print(cust.total_buy_product,cust.total_buy_amount)
