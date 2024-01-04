# from main import Ocean
from settings import Settings

class Fish :
    def __init__(self, position : tuple):
        self.position = position
    
    #def move(self, position):
    #je commence pour scaner les positions adjacentes
        # la position est donnée en parametre
        #pass
    def move_fishes(self, direction):
        #a faire plus tard: modalités de parcours des positions

        #récupération des cases adjaçentes
        '''north_position = (current_position[0] - 1, current_position[1])
        south_position = (current_position[0] + 1, current_position[1])
        west_position = (current_position[0], current_position[1] - 1)
        east_position = (current_position[0], current_position[1] + 1)'''
        #analyse des 4 positions=> dans un dictionnaire de 4 elts

        # north_position 
        

        if direction == "north_position":
            self.position [0] -= 1
        if direction =="south_position":
            self.position [0] += 1
        if direction =="west_position":
            self.position [1] -=1
        if direction =="east_position":
            self.position [1] += 1



        '''liste_positions = {'north_position': (current_position[0] - 1, current_position[1]),
        'south_position': (current_position[0] + 1, current_position[1]),
        'west_position': (current_position[0], current_position[1] - 1),
        'east_position': (current_position[0], current_position[1] + 1)
        }'''
        


        #recherche de la valeur(thon shark ou none?) correspondant à la position

        #en fonction de cette valeur :

        #si case vide j y vais ok pour thon et shark(meme si second choix)

        #si case idem je ne bouge pas ok pour thon et shark

        #si case differente :

        ##si thon si possible je bouge sinon c est quasiment mort== ne bouge pas
        ##si requin: j y vais et ma valeur remplace thon dans le tuple 
        #pass

#random pour si je suis un requin je vais ou si ya 3 thon devant moi
    def reproduce (self):
        pass


class Tuna (Fish) :
    pass


class Shark (Fish):
    energy = Settings.shark_energy

