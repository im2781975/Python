class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
class bus:
    def __init__(self, coach, driver, arrival, depart, from_dst, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.depart = depart
        self.from_dst = from_dst
        self.to = to
        self.seat = ["Empty" for i in range (20)]
b = bus(2, "abc", "13.00", "13.30", "Dhaka", "barisal")
class phitron:
    total_bus = 5
    total_bus_list = []
    def add_bus(self):
        bus_no = int(input("Enter:"))
        flag = 1
        for w in self.total_bus_list:
            if bus_no==w['coach']:
                print("Already added")
                flag = 0
                break
        if flag:
            bus_driver = input("Name: ")
            bus_arrival = input("Arrival time: ")
            bus_depart = input("Depart time: ")
            bus_from = input("From dst: ")
            bus_to = input("To dst: ")
            self.new_bus = bus(bus_no, bus_driver, bus_arrival, bus_depart, bus_from, bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("Added successfully")
class counter(phitron):
    user_list = []
    def reservation(self):
        bus_no = int(input("Enter: "))
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                passenger = input("Name: ")
                seat_no = int(input("seat_no: "))
                if seat_no > 20:
                    print("No seats avaiable")
                elif w['seat'][seat_no - 1]!= "Empty":
                    print("Already booked")
                else:
                    w['seat'][seat_no -1] = passenger
            else:
                print("No bus available")
        """for bus in self.total_bus_list:
            print(bus['seat'])"""
    def show_ticket(self):
        bus_no = int(input("Enter bus number: "))
        for w in self.total_bus_list:
            if bus_no==w['coach']:
                print(f"{bus['coach']} {bus['driver']} {bus['arrival']}")
                a=1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}.{w['seat'][a-1]}",end = "\t")
                        a+= 1
                    for j in range(2):
                        print(f"{a}.{w['seat'][a-1]}",end = "\t")
                        a+= 1
                    print()
    def get_user(self):
        return self.user_list
    def create_account(self):
        name = input("username: ")
        password= input("password: ")
        self.new_user = user(name, password)
        self.user_list.append(vars(self.new_user))
    def available_bus(self):
        if len(self.total_bus_list) == 0:
            print("Unavaiable bus")
        else:
            for bus in self.total_bus_list:
                print(f"{bus['coach']} {bus['driver']} {bus['arrival']}")
while(True):
    company = phitron()
    b = counter()
    print("1.create account")
    print("2.Login account")
    print("3.Exit")
    
    user_input = int(input("Enter choice: "))
    if user_input == 3:
        break
    elif user_input == 1:
        b.create_account()
    elif user_input == 2:
        name = input("username:")
        password = input("password:")
        flag = 0
        isAdmin = False
        if name ="admin" and password = "1234":
            isAdmin = True
        if isAdmin = False:
            for user in b.get_user:
                if user["username"] ==name and user["password"] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print("1.Available buses: ")
                    print("Show bus info: ")
                    print("3.Reservation: ")
                    print("4.Exit")
                a = int(input("Enter choice: "))
                if a==4:
                    break
                elif a==1:
                    b.available_bus()
                elif a==2:
                    b.show_ticket()
                elif a==3:
                    b.reservation()
            else:
                print("No username found")
        else:
            while True:
                print("1.show bus: ")
                print("2.available bus")
                print("3.show bus info")
                print("4.Exit")
                a = int(input("Enter choice: "))
                if a==4:
                    break
                elif a==2:
                    b.available_bus()
                elif a==1:
                    b.add_bus()
                elif a==3:
                    b.show_ticket()
            else:
                print("No username found")
#print(vars(b))
company = phitron()
company.add_bus()
c = counter()
c.reservation()
