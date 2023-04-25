import math

# Définition de la classe Forme
class Forme:
    # Méthode pour calculer l'aire (retourne 0 par défaut)
    def aire(self):
        return 0


# Définition de la classe Rectangle qui hérite de la classe Forme
class Rectangle(Forme):
    # Constructeur avec deux paramètres: largeur et hauteur
    def __init__(self, largeur, hauteur):
        # Attributs de la classe Rectangle
        self.largeur = largeur
        self.hauteur = hauteur
    
    # Redéfinition de la méthode aire de la classe Forme pour calculer l'aire du rectangle
    def aire(self):
        return self.largeur * self.hauteur


# Définition de la classe Cercle qui hérite de la classe Forme
class Cercle(Forme):
    # Constructeur avec un paramètre: rayon
    def __init__(self, rayon):
        # Attribut de la classe Cercle
        self.rayon = rayon
    
    # Redéfinition de la méthode aire de la classe Forme pour calculer l'aire du cercle
    def aire(self):
        return math.pi * self.rayon ** 2


# Création d'une instance de la classe Rectangle avec des dimensions de 5 et 10
rect = Rectangle(5, 10)

# Affichage de l'aire du rectangle (qui devrait être égale à 50)
print("Aire du rectangle:", rect.aire())


# Création d'une instance de la classe Cercle avec un rayon de 3
cercle = Cercle(3)

# Affichage de l'aire du cercle (qui devrait être d'environ 28.27)
print("Aire du cercle:", cercle.aire())