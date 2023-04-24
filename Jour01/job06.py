class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur # attribut privé de longueur
        self.__largeur = largeur # attribut privé de largeur

    def get_longueur(self):
        return self.__longueur # méthode pour récupérer la longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur # méthode pour modifier la longueur

    def get_largeur(self):
        return self.__largeur # méthode pour récupérer la largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur # méthode pour modifier la largeur

    def __str__(self):
        return f"Rectangle de longueur {self.__longueur} et de largeur {self.__largeur}" # méthode pour obtenir une description de l'objet

rectangle = Rectangle(10, 5)

print(rectangle) # affiche "Rectangle de longueur 10 et de largeur 5"

rectangle.set_longueur(30)
rectangle.set_largeur(15)

print(rectangle.get_longueur()) # affiche nouvelle valeur longueur
print(rectangle.get_largeur()) # affiche nouvelle valeur longueur