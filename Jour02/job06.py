class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque      # attribut "marque" de l'objet initialisé à la valeur passée en argument
        self.modele = modele      # attribut "modele" de l'objet initialisé à la valeur passée en argument
        self.annee = annee        # attribut "annee" de l'objet initialisé à la valeur passée en argument
        self.prix = prix          # attribut "prix" de l'objet initialisé à la valeur passée en argument
        
    def informationsVehicule(self):
        print("Marque:", self.marque)   # affichage de la marque de l'objet
        print("Modèle:", self.modele)   # affichage du modèle de l'objet
        print("Année:", self.annee)     # affichage de l'année de l'objet
        print("Prix: €", self.prix)     # affichage du prix de l'objet

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)           # appel du constructeur de la classe parente avec les arguments passés
        self.portes = portes                                    # initialisation de l'attribut "portes" propre à la classe Voiture
        
    def informationsVehicule(self):
        super().informationsVehicule()                          # appel de la méthode informationsVehicule de la classe parente
        print("Portes:", self.portes)                           # affichage du nombre de portes de la voiture

    def demarrer(self):
        print("La voiture démarre")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)           # appel du constructeur de la classe parente avec les arguments passés                                  
        self.roues = roues                                      # initialisation de l'attribut "roues" propre à la classe Moto
        
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Roues:", self.roues)

    def demarrer(self):
        print("La moto démarre")


# Création d'une instance de la classe Voiture avec les attributs passés en arguments
ma_voiture = Voiture("Mercedes", "Classe A", 2021, 18500, 4)

# Création d'une moto et affichage de ses informations
ma_moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)


# Appel de la méthode informationsVehicule des objets ma_voiture et ma_moto pour afficher leurs informations
ma_voiture.informationsVehicule()
ma_moto.informationsVehicule()

# Appel de la méthode demarrer des objets ma_voiture et ma_moto pour afficher leurs messages personalisés
ma_voiture.demarrer()
ma_moto.demarrer()