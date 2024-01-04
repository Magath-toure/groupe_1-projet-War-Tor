from models.fishes import Tuna, Shark, Fish
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
            available_positions = [key for key, value in ocean.ecosystem.items() if value is None]
            random_position = random.choice(available_positions)

            aleatoire = random.choice([1,2])
            if aleatoire == 1 and sharks_count < Settings.nb_sharks:
                self.ecosystem[random_position] = Shark(position=random_position)
                sharks_count += 1
            elif aleatoire == 2 and tunas_count < Settings.nb_tunas:
                self.ecosystem[random_position] = Tuna(position=random_position)
                tunas_count += 1
    
    '''def update_exosystem (self):

        # Mettre à jour l'écosystème en fonction des règles définies
        for i in range(Settings.ocean_height):
            for j in range(Settings.ocean_width):
                # Appliquer les règles pour le déplacement, la reproduction, etc.
                # en fonction du type de poisson à cette position (i, j)
                # Mettre à jour l'état des poissons dans l'écosystème'''




  
            

        #donner les instructions à suivre en fonction de la case

ocean = Ocean()
ocean.generate_fishes()
for i in range(Settings.ocean_height):
    ligne = ""
    for j in range(Settings.ocean_width):
        if isinstance (ocean.ecosystem[(i,j)], Tuna) :
            ligne += "T"
        elif isinstance (ocean.ecosystem[(i,j)], Shark) :
            ligne += "S"
        else:
            ligne += " "
    print(ligne)
    
tuna = Fish()
tuna.move_fishes()
for tuna in ocean.ecosystem :
    if isinstance (tuna[(i,j)]) :
        Fish.self.position [0] -= 1
        tuna.move()
    


# print(len(ocean.ecosystem))
# print(len([key for key, value in ocean.ecosystem.items() if isinstance(value, Shark)]))
# print(len([key for key, value in ocean.ecosystem.items() if isinstance(value, Tuna)]))



