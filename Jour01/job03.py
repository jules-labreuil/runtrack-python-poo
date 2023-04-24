class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        # Les arguments "nombre1" et "nombre2" sont des entiers.
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        # La variable "result" est un entier.
        resultat = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est :", resultat)

# Création d'une instance de la classe "Operation".
# Les arguments "nombre1" et "nombre2" sont tous deux des entiers.
operation = Operation(12, 3)

# Appel de la méthode "addition" sur l'instance "operation".
operation.addition()