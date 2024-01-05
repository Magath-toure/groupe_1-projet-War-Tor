from settings import Settings

class Fish:
    def __init__(self, position : tuple):
        self.position = position
    
    
    #je commence pour scaner les positions adjacentes
    #je code le movement ici:pas de probleme d import
    #je cree un dictionnaire un sous de cases adjacentes
    def check_adjacent_places(self, current_position : tuple):
        north_position = (current_position[0] - 1, current_position[1])
        south_position = (current_position[0] + 1, current_position[1])
        west_position = (current_position[0], current_position[1] - 1)
        east_position = (current_position[0], current_position[1] + 1)
        adjacent_positions = [north_position, south_position, east_position, west_position]                 
        return [key for key, value in self.ecosystem.items() if key in adjacent_positions]  
    
    # je cree le movement
    def move(self):
        #tant qu il reste des poissons

        #si la valeur de item[1] est Shark
        #si dabns les cases il y a des poissons, il y va de façon aleatoire
        #sinon rien


        #si la valeur de item[1] est Tuna
        #si dans les cases il ya du vide il y va de façon aléatoire
        pass


    def move_fishes(self, direction):
        


        
        
    
        pass

    def reproduce (self):
        pass


class Tuna (Fish) :
    #1/si case vide j y vais == ma position devient celle de la case vide
    
   
    pass


class Shark (Fish):
    energy = Settings.shark_energy

    #1/si case thon =,differente j y vais == ma position devient celle du thon, je remplace la valeur thon ds le tuple de cette position
    #2/sinon si case vide: je verifie les autres vases,1 er niveau par defaut ma position devient celle de la case vide j y vais

    pass
test = Fish()
test.check_adjacent_places((2,2))
