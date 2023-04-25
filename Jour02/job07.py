import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return "{} de {}".format(self.valeur, self.couleur)
    
class Jeu:
    def __init__(self):
        self.paquet = []
        for valeur in range(2, 11):
            for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:
                self.paquet.append(Carte(str(valeur), couleur))
        for valeur in ["Valet", "Dame", "Roi"]:
            for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:
                self.paquet.append(Carte(valeur, couleur))
        for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:
            self.paquet.append(Carte("As", couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()
    
def jouer_blackjack():
    jeu = Jeu()
    jeu.melanger()

    # Distribuer les cartes aux joueurs
    main_joueur = [jeu.tirer_carte(), jeu.tirer_carte()]
    main_croupier = [jeu.tirer_carte(), jeu.tirer_carte()]

    def calculer_total(main):
        total = 0
        as_count = 0
        for carte in main:
            if carte.valeur in ["Valet", "Dame", "Roi"]:
                total += 10
            elif carte.valeur == "As":
                as_count += 1
            else:
                total += int(carte.valeur)
        total += as_count
        while total + 10 <= 21 and as_count > 0:
            total += 10
            as_count -= 1
        return total

    def afficher_mains(joueur, croupier, montrer_toutes_cartes_croupier=False):
        print("Main du croupier:")
        if montrer_toutes_cartes_croupier:
            for carte in croupier:
                print(carte)
            print("Total:", calculer_total(croupier))
        else:
            print(croupier[0])
            print("Total:", calculer_total([croupier[0]]))
        print()
        print("Main du joueur:")
        for carte in joueur:
            print(carte)
        print("Total:", calculer_total(joueur))
        print()

    # Afficher les mains
    afficher_mains(main_joueur, main_croupier)

    # Le joueur joue
    while True:
        choix_joueur = input("Voulez-vous prendre une carte (p) ou passer (s)? ")
        if choix_joueur == "p":
            main_joueur.append(jeu.tirer_carte())
            afficher_mains(main_joueur, main_croupier)
            total_joueur = calculer_total(main_joueur)
            if total_joueur > 21:
                print("Vous avez dépassé 21! Vous avez perdu.")
                return
        elif choix_joueur == "s":
            break

    # Le croupier joue
    total_croupier = calculer_total(main_croupier)
    afficher_mains(main_joueur, main_croupier, True)
    while total_croupier < 17:
        print("Le croupier prend une carte...")
        main_croupier.append(jeu.tirer_carte())
        total_croupier = calculer_total(main_croupier)
        afficher_mains(main_joueur, main_croupier, True)

# Résultat de la partie
    total_joueur = calculer_total(main_joueur)
    total_croupier = calculer_total(main_croupier)
    if total_joueur > 21:
        print("Vous avez dépassé 21! Vous avez perdu.")
    elif total_croupier > 21:
        print("Le croupier a dépassé 21! Vous avez gagné.")
    elif total_joueur > total_croupier:
        print("Vous avez gagné!")
    elif total_croupier > total_joueur:
        print("Le croupier a gagné!")
    else:
        print("Égalité!")

# Lancer le jeu pour la première fois
print("Bienvenue au Julito's BlackJack !")
jouer_blackjack()

# Demander si le joueur veut jouer à nouveau
while True:
    rejouer = input("Voulez-vous jouer à nouveau? (o/n) ")
    if rejouer == "o":
        jouer_blackjack()
    elif rejouer == "n":
        print("Merci d'avoir joué!")
        break
    else:
        print("Veuillez entrer 'o' pour oui ou 'n' pour non.")
        continue  # continuer la boucle s'il y a une réponse invalide