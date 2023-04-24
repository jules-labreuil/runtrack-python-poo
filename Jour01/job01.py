class Operation:
    def __init__(self, nombre1: float = 0, nombre2: float = 0):
        # Initialise les attributs de l'objet
        self.nombre1 = nombre1  # attribut de type float, représente le premier nombre de l'opération (initialisé à 0)
        self.nombre2 = nombre2  # attribut de type float, représente le deuxième nombre de l'opération (initialisé à 0)

operation = Operation()
print(operation)  # Affiche l'objet de la classe Operation