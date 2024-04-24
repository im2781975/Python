class family:
    def __init__(self, address):
        self.address = address
class school:
    def __init__(self, id, level):
        self.id = id
        self.level = level
class sport:
    def __init__(self, game):
        self.game = game
class student(family, school, sport):
    def __init__(self, address, id, level, game):
        school().__init__(self, id, level)
        sport().__init__(self, game)
        super().__init__(address)
    
