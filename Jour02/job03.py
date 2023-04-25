class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # attribut privé longueur
        self.__largeur = largeur  # attribut privé largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)  # méthode calculant le périmètre
    
    def surface(self):
        return self.__longueur * self.__largeur  # méthode calculant la surface
    
    def get_longueur(self):
        return self.__longueur  # accesseur pour longueur
    
    def get_largeur(self):
        return self.__largeur  # accesseur pour largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur  # mutateur pour longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur  # mutateur pour largeur
        

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)  # appel du constructeur de la classe parent Rectangle
        self.__hauteur = hauteur  # attribut privé hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur  # méthode calculant le volume
    
    def get_hauteur(self):
        return self.__hauteur  # accesseur pour hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur  # mutateur pour hauteur


# Création d'un rectangle de longueur 5 et de largeur 3
mon_rectangle = Rectangle(5, 3)

# Affichage de la surface et du périmètre du rectangle
print("Surface :", mon_rectangle.surface())
print("Périmètre :", mon_rectangle.perimetre())

# Modification de la longueur du rectangle
mon_rectangle.set_longueur(8)
print("Nouvelle surface :", mon_rectangle.surface())


# Création d'un parallélépipède de longueur 5, de largeur 3 et de hauteur 2
mon_parallelepipede = Parallelepipede(5, 3, 2)

# Affichage de la surface, du périmètre et du volume du parallélépipède
print("Surface :", mon_parallelepipede.surface())
print("Périmètre :", mon_parallelepipede.perimetre())
print("Volume :", mon_parallelepipede.volume())

# Modification de la hauteur du parallélépipède
mon_parallelepipede.set_hauteur(4)
print("Nouveau volume :", mon_parallelepipede.volume())