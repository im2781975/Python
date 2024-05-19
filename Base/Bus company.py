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
                    
#print(vars(b))
company = phitron()
company.add_bus()
