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
print(vars(b))
