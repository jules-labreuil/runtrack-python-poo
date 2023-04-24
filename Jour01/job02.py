class Operation:
    def __init__(self, nombre1: int = 12, nombre2: int = 3):
        # Initialise les attributs de l'objet
        self.nombre1 = nombre1  # attribut de type int, représente le premier nombre de l'opération (initialisé à 12)
        self.nombre2 = nombre2  # attribut de type int, représente le deuxième nombre de l'opération (initialisé à 3)

operation = Operation()
print("Le nombre1 est", operation.nombre1)  # Affiche la valeur de l'attribut "nombre1"
print("Le nombre2 est", operation.nombre2)  # Affiche la valeur de l'attribut "nombre2"