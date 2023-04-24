class Student:
    def __init__(self, nom: str, prenom: str, id: int):
        # Initialise les attributs de l'objet
        self.__nom = nom  # attribut de type str, représente le nom de l'étudiant
        self.__prenom = prenom  # attribut de type str, représente le prénom de l'étudiant
        self.__id = id  # attribut de type int, représente l'identifiant de l'étudiant
        self.__credits = 0  # attribut de type int, représente le nombre de crédits acquis par l'étudiant (initialisé à 0)
        self.__level = None  # attribut de type None ou str, représente le niveau de l'étudiant (initialisé à None)

    def add_credits(self, id, credits):  # Définition de la méthode add_credits prenant en paramètres self (l'instance de la classe Student), id (le numéro d'étudiant) et credits (le nombre de crédits à ajouter)
        if id == self.__id and credits > 0:  # Vérification que le numéro d'étudiant correspond à celui de l'instance et que le nombre de crédits est supérieur à 0
            self.__credits += credits  # Ajout des crédits à l'attribut __credits de l'instance
            self.__level = self.__studentEval()  # Mise à jour du niveau de l'instance en appelant la méthode __studentEval()
        elif id != self.__id:  # Si le numéro d'étudiant ne correspond pas à celui de l'instance
            print("Le numéro d'étudiant ne correspond pas.")  # Affichage d'un message d'erreur
        else:  # Si le nombre de crédits est inférieur ou égal à 0
            print("Le nombre de crédits doit être supérieur à zéro.")  # Affichage d'un message d'erreur

    def __studentEval(self):
        if self.__credits >= 90:  # Vérification du nombre de crédits acquis pour déterminer le niveau
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom =", self.__nom)         # Affichage du nom de l'étudiant
        print("Prénom =", self.__prenom)   # Affichage du prénom de l'étudiant
        print("Id =", self.__id)           # Affichage de l'identifiant de l'étudiant
        print("Niveau =", self.__level)    # Affichage du niveau de l'étudiant

doe = Student("Doe", "John", 145)
dupont = Student("Dupont", "Jean", 142)

doe.add_credits(145, 30)    # Ajout de 30 crédits à l'étudiant 'doe' dont le numéro d'étudiant est bien le 145
doe.add_credits(145, 25)    # Ajout de 25 crédits à l'étudiant 'doe' dont le numéro d'étudiant est bien le 145
doe.add_credits(145, 20)    # Ajout de 20 crédits à l'étudiant 'doe' dont le numéro d'étudiant est bien le 145

dupont.add_credits(142, 30) # Ajout de 30 crédits à l'étudiant 'dupont' dont le numéro d'étudiant est bien le 142
dupont.add_credits(142, 25) # Ajout de 25 crédits à l'étudiant 'dupont' dont le numéro d'étudiant est bien le 142

doe.studentInfo()           # Affichage des informations sur l'étudiant 'doe'
dupont.studentInfo()        # Affichage des informations sur l'étudiant 'dupont'