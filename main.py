from models.fishes import Tuna, Shark
from settings import Settings
import random

class Ocean :

    def __init__(self) :
        self.width = Settings.ocean_width
        self.height = Settings.ocean_height
        self.ecosystem = {}

        for i in range(Settings.ocean_height):
            for j in range(Settings.ocean_width):
                self.ecosystem[(i,j)] = None

    def generate_fishes(self):
        sharks_count = 0
        tunas_count = 0
        # Tant que le nb de shark ou de tuna n'est pas atteint
        # continuer à choisir aléatoirement une case parmi les case innocupés et y mettre un shark ou un tuna
        while sharks_count < Settings.nb_sharks or tunas_count < Settings.nb_tunas:
            available_positions = [key for key, value in self.ecosystem.items() if value is None]
            random_position = random.choice(available_positions)

            aleatoire = random.choice([1,2])
            if aleatoire == 1 and sharks_count < Settings.nb_sharks:
                self.ecosystem[random_position] = Shark(position=random_position)
                sharks_count += 1
            elif aleatoire == 2 and tunas_count < Settings.nb_tunas:
                self.ecosystem[random_position] = Tuna(position=random_position)
                tunas_count += 1

    



""" ocean = Ocean()
ocean.generate_fishes()
print(len(ocean.ecosystem))
print(len([key for key, value in ocean.ecosystem.items() if isinstance(value, Shark)]))
print(len([key for key, value in ocean.ecosystem.items() if isinstance(value, Tuna)])) """



