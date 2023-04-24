class Animal:
    def __init__(self):  # Constructeur prenant aucun paramètre
        self.age = 0  # initialisation de l'attribut age à 0
        self.prenom = ""  # initialisation de l'attribut prenom à une chaine de caractère vide

    def __str__(self):  # Méthode magique qui permet de renvoyer une description de l'objet sous forme de chaine de caractères
        return "L'animal se nomme{}".format(self.prenom)
    
    def vieillir(self):  # Méthode qui permet d'incrémenter l'attribut age de l'objet de 1
        self.age += 1
    
    def nommer(self, nom):  # Méthode qui permet d'attribuer un nom à l'objet
        self.prenom = nom
    
# Instanciation de l'objet animal
animal = Animal()

# Attribution d'un nom à l'animal
animal.nommer("Luna")

# Affichage de l'attribut age initialisé à zéro
print("Âge initial de l'animal :", animal.age)

# Faire vieillir l'animal
animal.vieillir()

# Affichage de l'âge après vieillissement
print("Nouvel âge de l'animal :", animal.age)

# Affichage du nom de l'animal
print(animal)