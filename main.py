import random
from models.fishes import Tuna, Shark
from settings import Settings

class Ocean :

    def __init__(self) :
        self.width = Settings.ocean_width
        self.height = Settings.ocean_height
        self.ecosystem = {}

    def generate_fishes(self):
        compteur = 0

        # TANT QUE je ne dépasse pas le nombre maximum de Fish
        # Je générer des poissons ou des cases vides
        for i in range(self.height):
            for j in range(self.width):
                aleatoire = random.choice([1,2,3])
                if aleatoire == 1:
                    self.ecosystem[(i,j)] = Tuna(position=(i,j))
                    compteur += 1
                elif aleatoire == 2:
                    self.ecosystem[(i,j)] = Shark(position=(i,j))
                    compteur += 1
                elif aleatoire == 3:
                    None
            
            
ocean = Ocean()
ocean.generate_fishes()
print(len(ocean.ecosystem))