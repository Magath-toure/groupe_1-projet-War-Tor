import os
#import colored
from colorama import Fore, Style
from models.fishes import Tuna, Shark, Fish
from settings import Settings
import random
import time


class Bcolors :
    red = '\033[91m'
    blue = '\033[96m'
    green = '\033[92m'


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

    def display_ecosystem(self):
        #print("Number of sharks : ", len([key for key, value in self.ecosystem.items() if isinstance(value, Shark)]))
        #print("Number of tunas : ", len([key for key, value in self.ecosystem.items() if isinstance(value, Tuna)]))
        
        for i in range(Settings.ocean_height):
            ligne = ""
            for j in range(Settings.ocean_width):
                if isinstance (ocean.ecosystem[(i,j)], Tuna) :
                    ligne += f"{Fore.GREEN}T{Style.RESET_ALL}"
                elif isinstance (ocean.ecosystem[(i,j)], Shark) :
                    ligne += f"{Fore.RED}S{Style.RESET_ALL}"
                else:
                    ligne += " "
            print(ligne)
    
        '''
        for i in range(Settings.ocean_height):
            line_fishes = []
            for j in range(Settings.ocean_width):
                to_add = None if self.ecosystem[(i,j)] is None else type(self.ecosystem[(i,j)]).__name__
                line_fishes.append(to_add)
            print(line_fishes) 
            '''
        

    #methode qui lance le mouvement perpetuel vers une case vide
    def move_fish_to_empty(self):
        while True:
            #deplacer l ensemble des poissons vers une case vide adjacente
            for elt in self.ecosystem.items():
                if elt[1] is not None:
                    elt[1].move(self.ecosystem)                    
            os.system('cls' if os.name == 'nt' else 'clear')        

            self.display_ecosystem()
            time.sleep(1)


    
ocean = Ocean()
ocean.generate_fishes()
ocean.display_ecosystem()
ocean.move_fish_to_empty()



