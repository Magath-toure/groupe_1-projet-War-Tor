
from settings import Settings

class Fish :
    def __init__(self, position : tuple):
        self.position = position
    
    def move (self):
        pass

    def reproduce (self):
        pass


class Tuna (Fish) :
    pass


class Shark (Fish):
    energy = Settings.shark_energy

