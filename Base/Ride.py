
from abc import ABC,abstractmethod
class user:
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email 
        self.__id = 0
        self.__nid = nid
        self.wallet = 0
    @abstractmethod
    def display(self):
        raise NotImplementedError
class rider(user):
    def __init__(self, name, email, nid):
        self.cur_ride = None
        super().__init__(name, email, nid)
    def display(self):
        print(f'{self.name} {self.email} {self.nid}')
    def request_ride(self, location, destination):
        if not self.cur_ride:
            # TODO : set ride properly
            # TODO : set cur ride via ride match
            ride_request = None
            self.cur_ride = None
class driver(user):
    def __init__(self, name, email, nid, cur_loc):
        super().__init__(name, email, nid):
        self.cur_loc = cur_loc
    def display(self):
        print(f'{self.name} {self
        .email} {self.nid}')
    def accept_ride(self, ride):
        ride.set_driver(self)
