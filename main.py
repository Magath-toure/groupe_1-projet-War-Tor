import random
from models.fishes import Tuna, Shark
from settings import Settings

class Ocean :

    def __init__(self) :
        self.width = Settings.ocean_width
        self.height = Settings.ocean_height
        self.ecosystem = {}

    def generate_fishes(self):
        compteur_tuna = 0
        compteur_shark = 0
        
        # TANT QUE je ne dépasse pas le nombre maximum de Fish
        # Je générer des poissons ou des cases vides
        for i in range(self.height):
            for j in range(self.width):
                aleatoire = random.choice([1,2,3])
                if aleatoire == 1 and compteur_tuna <= Settings.nb_tunas:
                    self.ecosystem[(i,j)] = Tuna(position=(i,j))
                    compteur_tuna += 1
                    #une fois nb_tuna atteint, il faut stopper la generation de tuna
                elif aleatoire == 2 and compteur_shark <= Settings.nb_sharks:
                    self.ecosystem[(i,j)] = Shark(position=(i,j))
                    compteur_shark += 1
                elif aleatoire == 3:
                    None

        print("NB Tunas : ", compteur_tuna)
        print("NB Shark : ", compteur_shark)


ocean = Ocean()
ocean.generate_fishes()

print(len(ocean.ecosystem))