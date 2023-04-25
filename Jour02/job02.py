class Personne:
    def __init__(self, age=14): # constructeur de la classe avec un paramètre âge (par défaut 14)
        self.age = age # initialisation de l'attribut age
        
    def afficherAge(self): # méthode pour afficher l'âge
        print(f"J'ai {self.age} ans")
        
    def bonjour(self): # méthode pour saluer
        print("Hello")
        
    def modifierAge(self, new_age): # méthode pour modifier l'âge
        self.age = new_age
        
    
class Eleve(Personne): # classe qui hérite de la classe Personne
    def allerEnCours(self): # méthode spécifique pour les élèves
        print("Je vais en cours")
        
    def affichageAge(self): # méthode pour afficher l'âge de l'élève
        print(f"J'ai {self.age} ans")
        
        
class Professeur(Personne): # classe qui hérite de la classe Personne
    def __init__(self, matiereEnseignee, age=30): # constructeur de la classe avec un paramètre matiereEnseignee et un paramètre âge (par défaut 30)
        super().__init__(age) # appel du constructeur de la classe parente pour initialiser l'attribut age
        self.__matiereEnseignee = matiereEnseignee # initialisation de l'attribut matiereEnseignee (marqué comme privé)
        
    def enseigner(self): # méthode spécifique pour les professeurs
        print("Le cours va commencer")
        

personne = Personne() # création d'une instance de la classe Personne
eleve = Eleve() # création d'une instance de la classe Eleve

print(eleve.age) # affiche l'âge de l'élève (par défaut 14)

personne = Personne()
eleve = Eleve()
eleve.bonjour() # affiche "Hello"
eleve.allerEnCours() # affiche "Je vais en cours"
eleve.modifierAge(15) # change l'âge de l'élève à 15 ans

professeur = Professeur("Mathématiques", 40)
professeur.bonjour() # affiche "Hello"
professeur.enseigner() # affiche "Le cours va commencer"