#from settings import Settings

import random


class Fish:
    def __init__(self, position : tuple):
        self.position = position
    
    
    #je commence pour scaner les positions adjacentes
    #je code le movement ici:pas de probleme d import
    #je cree un dictionnaire un sous de cases adjacentes
    def check_adjacent_places(self):
        north_position = (self.position[0] - 1, self.position[1])
        south_position = (self.position[0] + 1, self.position[1])
        west_position = (self.position[0], self.position[1] - 1)
        east_position = (self.position[0], self.position[1] + 1)
        adjacent_positions = [north_position, south_position, east_position, west_position]
        return adjacent_positions                 
        #return [key for key, value in ecosystem.items() if key in adjacent_positions]  
    
    # je cree le movement perpetuel
    def move(self, ecosystem : dict):
        #faire bouger le poisson vers une classe vide
       
        #quelles sont les emplacements vides dans les positions adjacentes fournies par le scan
        #element = (position_1, ecosystem[position_1])        
        elements = [(key, value) for key, value in ecosystem.items() if value is None and key in self.check_adjacent_places()]
           
        
       # un des éléments prend la valeur Thon ou Requin et la position initiale à une valeur qui passe a None
        if len(elements) != 0:       
            choix = random.choice(elements)
            old_position = self.position
            self.position = choix[0]

            # deplacer le poisson à la nouvelle position
            ecosystem[self.position] = self
            # mettre un None à l'ancienne position
            ecosystem[old_position] = None


    def reproduce (self):
        pass


class Tuna (Fish) :
    #1/si case vide j y vais == ma position devient celle de la case vide
    
   
    pass


class Shark (Fish):


    #1/si case thon =,differente j y vais == ma position devient celle du thon, je remplace la valeur thon ds le tuple de cette position
    #2/sinon si case vide: je verifie les autres vases,1 er niveau par defaut ma position devient celle de la case vide j y vais

    pass
test = Fish((2,2))
print(test.check_adjacent_places())
test.move({})
