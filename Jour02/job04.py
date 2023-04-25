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


# Création d'une instance de la classe Rectangle avec des dimensions de 5 et 10
rect = Rectangle(5, 10)

# Affichage de l'aire du rectangle (qui devrait être égale à 50)
print(rect.aire()) # affiche 50