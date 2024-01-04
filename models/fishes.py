<<<<<<< HEAD
#from main import Ocean
=======
>>>>>>> main
from settings import Settings

class Fish:
    def __init__(self, position : tuple):
        self.position = position
    
    #def move(self, position):
    #je commence pour scaner les positions adjacentes
        # la position est donnée en parametre    
        #pass
    def move_fishes(self, current_position):
        #a faire plus tard: modalités de parcours des positions
        #tous les thons puis tous les requins

        #récupération des cases adjaçentes
        north_position = (current_position[0] - 1, current_position[1])
        south_position = (current_position[0] + 1, current_position[1])
        west_position = (current_position[0], current_position[1] - 1)
        east_position = (current_position[0], current_position[1] + 1)
        #analyse des 4 positions=> dans un dictionnaire de 4 elts

        #recherche de la valeur(thon shark ou none?) correspondant à la position

        #en fonction de cette valeur :

        #si case vide j y vais ok pour thon et shark(meme si second choix)

        #si case idem je ne bouge pas ok pour thon et shark

        #si case differente :

        ##si thon si possible je bouge sinon c est quasiment mort== ne bouge pas
        ##si requin: j y vais et ma valeur remplace thon dans le tuple 
        pass

    def reproduce (self):
        pass


class Tuna (Fish) :
    #1/si case vide j y vais == ma position devient celle de la case vide
    #2/si case idem =thon je n y vais pas == ma positipon reste identique
    #3/si case requin ? 1 er niveau je ne fais rien

    #si case differente :
    ##si thon si possible je bouge sinon c est quasiment mort== ne bouge pas
 
    pass


class Shark (Fish):
<<<<<<< HEAD
    energy = Settings.shark_energy

    #1/si case thon =,differente j y vais == ma position devient celle du thon, je remplace la valeur thon ds le tuple de cette position
    #2/sinon si case vide: je verifie les autres vases,1 er niveau par defaut ma position devient celle de la case vide j y vais
    #3/sinon si case idem = requin : je ny vais pas ma position reste identique

    #si case differente :
    ##si requin: j y vais et ma valeur remplace thon dans le tuple 
    #choix prioritaire
    pass
=======
    energy = Settings.shark_energy
>>>>>>> main
