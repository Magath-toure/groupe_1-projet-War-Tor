import random
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


class Ocean :

    def __init__(self) :
        self.width = Settings.ocean_width
        self.height = Settings.ocean_height
        self.grid = {}

    def generate_fishes(self):
        i = 0
        j = 0
        compteur = 0

        # TANT QUE je ne dépasse pas le nombre maximum de Fish
        # Je générer des poissons ou des cases vides
        while i < self.height:
            while j < self.width:
                aleatoire = random.choice([1,2,3])
                if aleatoire == 1:
                    self.grid[(i,j)] = Tuna(position=(i,j))
                    compteur += 1
                elif aleatoire == 2:
                    self.grid[(i,j)] = Shark(position=(i,j))
                    compteur += 1
                elif aleatoire == 3:
                    None
                j += 1

            i += 1
            j = 0

            
ocean = Ocean()
ocean.generate_fishes()
print(len(ocean.grid))