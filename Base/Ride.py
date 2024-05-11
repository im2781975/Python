from abc import ABC,abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.drivers = []
        self.riders = []
        self.rides = []
    def add_rider(self, rider):
        self.riders.append(rider)
    def add_driver(self, driver):
        self.drivers.append(driver)
    def __repr__(self) ->str:
        return f'{self.company_name} {len(self.drivers)} {len(self.riders)} '
class user:
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email 
        self.__id = 0
        self.__nid = nid
        self.wallet = 0
    @abstractmethod
    def display(self):
        raise NotImplmentedError
class rider(user):
    def __init__(self, name, email, nid, cur_loc):
        self.cur_ride = None
        self.wallet = 0
        self.cur_loc = cur_loc
        super().__init__(name, email, nid)
    def update_loc(self, cur_loc):
        self.cur_loc = cur_loc
    def load_cash(self, amount):
        if amount > 0:
            wallet += amount
    def display(self):
        print(f'{self.name} {self.email} {self.nid}')
    def request_ride(self,ride_sharing, destination):
        if not self.cur_ride:
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            self.cur_ride = ride_matcher.find_driver(ride_request)
            print(ride)
            self.cur_ride = ride
    def show_cur_ride(self):
        print(self.cur_ride)
class driver(user):
    def __init__(self, name, email, nid, cur_loc):
        super().__init__(name, email, nid):
        self.cur_loc = cur_loc
        self.wallet = 0
    def display(self):
        print(f'{self.name} {self
        .email}')
    def accept_ride(self, ride):
        ride.set_driver(self)
class Ride:
    def __init__(self, start_loc, end_loc):
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.start_time = None
        self.end_time = None
        self.driver = None
        self.rider = None
        self.estimated_fare = None
    def set_driver(self, driver):
        self.set_driver = driver
    def start_ride(self):
        self.start_time = datetime.now()
    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= estimated_fare
        self.driver.wallet += estimated_fare
    def __repr__(self):
        return f'{self.start_loc} {self.end_loc} '
class Ride_Request:
    def __init__(self, rider, end_loc):
        self.rider = rider
        self.end_loc = end_loc
class Ride_Matching:
    def __init__(self)->None:
        self.available_drivers = drivers
    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            # TODO : find the closest driver of the rider
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.cur_loc, ride_request.end_loc)
            driver.accept_ride(ride)
            return ride
class Vehicle(ABC):
    speed = {
        'car' = 50,
        'bike' = 60,
        'cng' = 15
    }
    def __init__(self, vehicle_type, licence_plate, rate):
        self.vehicle_type = vehicle_type
        self.licence_plate = licence_plate
        self.rete = rate
        self.status = 'available'
    @abstractmethod
    def start_drive(self):
        pass
class car(Vehicle):
    def __init__(self, vehicle_type, licence_type, rate):
        super().__init__(vehicle_type, licence_type, rate)
    def start_drive(self):
        self.status = 'busy'
class bike(Vehicle):
    def __init__(self, vehicle_type, licence_type, rate):
        super().__init__(vehicle_type, licence_type, rate)
    def start_drive(self):
        self.status = 'busy'
pathao = Ride_sharing('Pathao')
sakib = rider("A", 'B', 1234, 'D')
pathao.add_rider(sakib)
hasan = driver("E", 'F', 5678, 'G')
pathao.add_driver(hasan)
print(pathao)
sakib.request_ride(pathao, 'Uttara')
sakib.show_cur_ride()
