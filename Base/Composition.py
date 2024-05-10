class Engine:
    def __init__(self) ->None:
        pass
    def start(self):
        return f'Engine Started'
class Driver:
    def __init__(self) ->None:
        pass
#car Has a engine
class car:
    def __init__(self)->None:
        self.engine = Engine()
        self.driver = Driver()
    def start(self):
        self.engline.start()

class CPU:
    def __init__(self, core)->None:
        self.core = core
class Ram:
    def __init__(self, size)->None:
        self.size = size
class HardDrive:
    def __init__(self, cap)->None:
        self.cap = cap
class computer:
    def __init__(self, core, size, cap)->None:
        self.core = CPU(core)
        self.size = Ram(size)
        self.cap = HardDrive(cap)
mac = computer(8, 16, 512)
print(mac.size)
