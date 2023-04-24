class Personne:
    def __init__(self, nom: str, prenom: str):
        # L'argument "nom" est une chaîne de caractères représentant le nom de la personne.
        self.nom = nom
        # L'argument "prenom" est une chaîne de caractères représentant le prénom de la personne.
        self.prenom = prenom
    
    def SePresenter(self) -> str:
        # La méthode "SePresenter" renvoie une chaîne de caractères contenant le nom et le prénom de la personne.
        return f"Je m'appelle {self.prenom} {self.nom}."
    
# Création de deux instances de la classe "Personne".
# Les arguments "nom" et "prenom" sont tous deux des chaînes de caractères.
personne1: Personne = Personne("Doe", "John")
personne2: Personne = Personne("Dupont", "Jean")

# Appel de la méthode "SePresenter" sur chaque instance de la classe "Personne".
print(personne1.SePresenter())
print(personne2.SePresenter())