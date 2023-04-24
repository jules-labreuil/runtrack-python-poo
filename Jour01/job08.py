class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre  # titre du livre
        self.__auteur = auteur  # nom de l'auteur
        self.__nb_pages = nb_pages  # nombre de pages
        self.__disponible = True  # disponibilité du livre

    def get_titre(self):
        return self.__titre  # retourne le titre du livre

    def set_titre(self, titre):
        self.__titre = titre  # modifie le titre du livre

    def get_auteur(self):
        return self.__auteur  # retourne le nom de l'auteur du livre

    def set_auteur(self, auteur):
        self.__auteur = auteur  # modifie le nom de l'auteur du livre

    def get_nb_pages(self):
        return self.__nb_pages  # retourne le nombre de pages du livre

    def set_nb_pages(self, nb_pages):
        # Vérifie si nb_pages est un entier positif
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            # Affiche un message d'erreur si nb_pages n'est pas un entier positif
            print("Le nombre de pages doit être un nombre entier positif.")

    def est_disponible(self):
        return self.__disponible # Définition de la méthode pour savoir si le livre est disponible

    def emprunter(self):
        if self.est_disponible():  # Vérifie si le livre est disponible avant de l'emprunter
            self.__disponible = False  # Passe le livre en mode "emprunté"
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.est_disponible():  # Vérifie si le livre est déjà emprunté avant de le rendre
            self.__disponible = True  # Passe le livre en mode "disponible"
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre était déjà disponible.")

    def __str__(self):
        if self.est_disponible():  # Vérifie si le livre est disponible avant de l'afficher
            return f"Ce livre s'appelle {self.__titre}, il a été écrit par {self.__auteur}, comporte {self.__nb_pages} pages et est disponible"
        else:
            return f"Ce livre s'appelle {self.__titre}, il a été écrit par {self.__auteur}, comporte {self.__nb_pages} pages et n'est pas disponible"

livre = Livre("Le Seigneur des anneaux - La communauté de l'anneau", "J.R.R. Tolkien", 722)  # Crée une instance de la classe Livre

print(livre)           # appel de la méthode __str__() de l'objet livre pour afficher ses attributs

livre.emprunter()      # appel de la méthode emprunter() de l'objet livre pour le rendre indisponible
print(livre)           # appel de la méthode __str__() de l'objet livre pour afficher ses attributs mis à jour

livre.rendre()         # appel de la méthode rendre() de l'objet livre pour le rendre disponible
print(livre)           # appel de la méthode __str__() de l'objet livre pour afficher ses attributs mis à jour