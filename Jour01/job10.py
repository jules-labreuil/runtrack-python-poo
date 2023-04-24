class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir, en_marche=False):
        self.__marque = marque  # chaîne de caractères : la marque de la voiture
        self.__modele = modele  # chaîne de caractères : le modèle de la voiture
        self.__annee = annee  # entier : l'année de fabrication de la voiture
        self.__kilometrage = kilometrage  # entier : le nombre de kilomètres parcourus par la voiture
        self.__reservoir = reservoir  # entier : la capacité du réservoir de la voiture en litres
        self.__en_marche = en_marche  # booléen : indique si la voiture est en marche ou pas (défaut : éteinte)

    def get_marque(self):
        return self.__marque  # renvoie la marque de la voiture

    def set_marque(self, marque):
        self.__marque = marque  # met à jour la marque de la voiture

    def get_modele(self):
        return self.__modele  # renvoie le modèle de la voiture

    def set_modele(self, modele):
        self.__modele = modele  # met à jour le modèle de la voiture

    def get_annee(self):
        return self.__annee  # renvoie l'année de fabrication de la voiture

    def set_annee(self, annee):
        self.__annee = annee  # met à jour l'année de fabrication de la voiture

    def get_kilometrage(self):
        return self.__kilometrage  # renvoie le nombre de kilomètres parcourus par la voiture

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage  # met à jour le nombre de kilomètres parcourus par la voiture

    def get_en_marche(self):
        return self.__en_marche  # renvoie l'état de marche de la voiture (True = en marche, False = éteinte)

    def demarrer(self):
        if self.__verifier_plein():  # si le réservoir est suffisamment plein (plus de 5 litres)
            self.__en_marche = True  # on passe la voiture en mode "en marche"
            print("La voiture a assez d'essence pour démarrer.")  # on affiche un message de confirmation
        else:
            print("*** ATTENTION *** Quantité d'essence insuffisante, la voiture ne peut pas démarrer.")  # sinon on affiche un message d'erreur

    def arreter(self):
        self.__en_marche = False  # on passe la voiture en mode "éteinte"
        print("La voiture a été arrêtée.")  # on affiche un message de confirmation

    def __verifier_plein(self):
        if self.__reservoir > 5:  # si le réservoir contient plus de 5 litres
            return True  # on retourne True (le réservoir est suffisamment plein)
        else:
            return False  # sinon on retourne False (le réservoir est trop vide)
    
    def get_reservoir(self):
        return self.__reservoir

    def set_reservoir(self, quantite):
        self.__reservoir = quantite

    def info_voiture(self):
        print("Marque =", self.__marque)                # Affichage de la marque de la voiture
        print("Modèle =", self.__modele)                # Affichage du modèle de la voiture
        print("Année =", self.__annee)                  # Affichage de l'année la voiture

    def variables_voiture(self):
        print("Kilométrage =", self.__kilometrage)      # Affichage du kilométrage de la voiture
        print("Essence restante =", self.__reservoir)   # Affichage du nombre de litres d'essence restants
        
voiture = Voiture("Audi", "RS6", 2020, 10000, 50)

voiture.info_voiture()
voiture.variables_voiture()

voiture.set_kilometrage(15000)
print(f"MAJ COMPTEUR KILOMETRIQUE OK.")

voiture.set_reservoir(4)                                # Met à jour la quantité de carburant dans le réservoir
print(f"MAJ ESSENCE RESTANTE OK.")

voiture.variables_voiture()                             # Affiche les compteurs kilométriques et d'essences mis à jour
voiture.demarrer()                                      # Affiche si la voiture peut démarrer ou non