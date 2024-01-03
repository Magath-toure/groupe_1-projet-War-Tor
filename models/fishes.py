from main import Ocean
from settings import Settings

class Fish:
    def __init__(self, position : tuple):
        self.position = position
    
    #def move(self, position):
    #je commence pour scaner les positions adjacentes
        # la position est donnée en parametre    
        #pass
    def move_fishes(self, current_position):
        
        #récupération des cases adjaçentes
        north_position = (current_position[0] - 1, current_position[1])
        south_position = (current_position[0] + 1, current_position[1])
        west_position = (current_position[0], current_position[1] - 1)
        east_position = (current_position[0], current_position[1] + 1)
        pass

    def reproduce (self):
        pass


class Tuna (Fish) :
    pass


class Shark (Fish):
    energy = Settings.shark_energy
