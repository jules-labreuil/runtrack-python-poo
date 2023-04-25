import random

class Carte:
    def __init__(self, valeur, couleur):  # Définition de la classe Carte avec une méthode d'initialisation prenant une valeur et une couleur en argument
        self.valeur = valeur  # Définition d'un attribut "valeur" pour chaque instance de la classe Carte
        self.couleur = couleur  # Définition d'un attribut "couleur" pour chaque instance de la classe Carte

    def __str__(self):  # Définition d'une méthode de représentation de la carte en chaîne de caractères
        return "{} de {}".format(self.valeur, self.couleur)
    
class Jeu:
    def __init__(self):  # Définition de la classe Jeu avec une méthode d'initialisation qui crée un paquet de cartes
        self.paquet = []  # Initialisation d'une liste vide pour stocker les cartes
        for valeur in range(2, 11):  # Boucle sur les valeurs de 2 à 10
            for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:  # Boucle sur les couleurs
                self.paquet.append(Carte(str(valeur), couleur))  # Ajout d'une carte de la valeur et de la couleur courantes
        for valeur in ["Valet", "Dame", "Roi"]:  # Boucle sur les valeurs "Valet", "Dame", "Roi"
            for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:  # Boucle sur les couleurs
                self.paquet.append(Carte(valeur, couleur))  # Ajout d'une carte de la valeur et de la couleur courantes
        for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:  # Boucle sur les couleurs
            self.paquet.append(Carte("As", couleur))  # Ajout d'une carte As de la couleur courante

    def melanger(self):  # Définition d'une méthode pour mélanger le paquet de cartes
        random.shuffle(self.paquet)  # Utilisation de la fonction shuffle() du module random pour mélanger la liste de cartes

    def tirer_carte(self):  # Définition d'une méthode pour tirer une carte du paquet
        return self.paquet.pop()  # Utilisation de la méthode pop() pour retirer et renvoyer la dernière carte de la liste
    
def jouer_blackjack():  # Définition d'une fonction pour jouer au blackjack
    jeu = Jeu()  # Création d'un objet Jeu pour le paquet de cartes
    jeu.melanger()  # Mélange des cartes du paquet

    # Distribuer les cartes aux joueurs
    main_joueur = [jeu.tirer_carte(), jeu.tirer_carte()]
    main_croupier = [jeu.tirer_carte(), jeu.tirer_carte()]

    def calculer_total(main):  # Définition d'une fonction nommée calculer_total qui prend un argument appelé main
        total = 0  # Initialisation de la variable total à 0
        as_count = 0  # Initialisation de la variable as_count à 0
        for carte in main:  # Boucle pour chaque élément (carte) de la liste main
            if carte.valeur in ["Valet", "Dame", "Roi"]:  # Condition : si la valeur de la carte est dans la liste ["Valet", "Dame", "Roi"]
                 total += 10  # Ajoute 10 à la variable total
            elif carte.valeur == "As":  # Sinon, si la valeur de la carte est "As"
                 as_count += 1  # Ajoute 1 à la variable as_count
            else:  # Sinon (la valeur de la carte est un nombre)
                total += int(carte.valeur)  # Ajoute la valeur de la carte (convertie en entier) à la variable total
        total += as_count  # Ajoute la valeur de la variable as_count à la variable total
        while total + 10 <= 21 and as_count > 0:  # Tant que la somme de total et 10 est inférieure ou égale à 21 et as_count est supérieur à 0
            total += 10  # Ajoute 10 à la variable total
            as_count -= 1  # Soustrait 1 à la variable as_count
        return total  # Retourne la valeur de la variable total à l'appelant de la fonction

    def afficher_mains(joueur, croupier, montrer_toutes_cartes_croupier=False):  # Définition d'une fonction nommée afficher_mains qui prend trois arguments : joueur, croupier et montrer_toutes_cartes_croupier (qui a une valeur par défaut False)
        print("Main du croupier:")  # Affiche le texte "Main du croupier:"
        if montrer_toutes_cartes_croupier:  # Si montrer_toutes_cartes_croupier est True
            for carte in croupier:  # Boucle pour chaque élément (carte) de la liste croupier
                print(carte)  # Affiche la carte
            print("Total:", calculer_total(croupier))  # Affiche le texte "Total:" suivi de la valeur retournée par la fonction calculer_total appliquée à la liste croupier
        else:  # Sinon (montrer_toutes_cartes_croupier est False)
            print(croupier[0])  # Affiche la première carte de la liste croupier
            print("Total:", calculer_total([croupier[0]]))  # Affiche le texte "Total:" suivi de la valeur retournée par la fonction calculer_total appliquée à une liste contenant uniquement la première carte de la liste croupier
        print()  # Affiche une ligne vide
        print("Main du joueur:")  # Affiche le texte "Main du joueur:"
        for carte in joueur: # Boucle pour chaque élément (carte) de la liste joueur
            print(carte) # Affiche la carte
        print("Total:", calculer_total(joueur)) # Affiche le texte "Total:" suivi de la valeur retournée par la fonction calculer_total appliquée à la liste joueur
        print() # Affiche une ligne vide


    # Afficher les mains
    afficher_mains(main_joueur, main_croupier)

    # Le joueur joue
    while True:
        choix_joueur = input("Voulez-vous prendre une carte (p) ou passer (s)? ")  # Demande au joueur s'il veut prendre une carte (p) ou passer (s) et stocke la réponse dans la variable choix_joueur
        if choix_joueur == "p":  # Si le choix du joueur est de prendre une carte
            main_joueur.append(jeu.tirer_carte())  # Ajoute une carte tirée au hasard du jeu à la main du joueur
            afficher_mains(main_joueur, main_croupier)  # Affiche les mains du joueur et du croupier
            total_joueur = calculer_total(main_joueur)  # Calcule le total de la main du joueur en utilisant la fonction calculer_total() et stocke le résultat dans la variable total_joueur
            if total_joueur > 21:  # Si le total de la main du joueur est supérieur à 21
                print("Vous avez dépassé 21! Vous avez perdu.")  # Affiche un message indiquant que le joueur a perdu
                return  # Quitte la fonction
        elif choix_joueur == "s":  # Si le choix du joueur est de passer
            break  # Sort de la boucle while

    # Le croupier joue
    total_croupier = calculer_total(main_croupier)  # Calcule le total de la main du croupier en utilisant la fonction calculer_total() et stocke le résultat dans la variable total_croupier
    afficher_mains(main_joueur, main_croupier, True)  # Affiche les mains du joueur et du croupier en montrant toutes les cartes du croupier
    while total_croupier < 17:  # Tant que le total de la main du croupier est inférieur à 17
        print("Le croupier prend une carte...")  # Affiche un message indiquant que le croupier prend une carte
        main_croupier.append(jeu.tirer_carte())  # Ajoute une carte tirée au hasard du jeu à la main du croupier
        total_croupier = calculer_total(main_croupier)  # Calcule le total de la main du croupier en utilisant la fonction calculer_total() et stocke le résultat dans la variable total_croupier
        afficher_mains(main_joueur, main_croupier, True)  # Affiche les mains du joueur et du croupier en montrant toutes les cartes du croupier

    # Résultat de la partie
    total_joueur = calculer_total(main_joueur)  # Calculer le total de la main du joueur
    total_croupier = calculer_total(main_croupier)  # Calculer le total de la main du croupier
    if total_joueur > 21:  # Si le total de la main du joueur est supérieur à 21
        print("Vous avez dépassé 21! Vous avez perdu.")  # Afficher un message indiquant que le joueur a perdu
    elif total_croupier > 21:  # Sinon, si le total de la main du croupier est supérieur à 21
        print("Le croupier a dépassé 21! Vous avez gagné.")  # Afficher un message indiquant que le joueur a gagné
    elif total_joueur > total_croupier:  # Sinon, si le total de la main du joueur est supérieur au total de la main du croupier
        print("Vous avez gagné!")  # Afficher un message indiquant que le joueur a gagné
    elif total_croupier > total_joueur:  # Sinon, si le total de la main du croupier est supérieur au total de la main du joueur
        print("Le croupier a gagné!")  # Afficher un message indiquant que le joueur a perdu
    else:  # Sinon (les totaux sont égaux)
        print("Égalité!")  # Afficher un message indiquant qu'il y a une égalité

# Lancer le jeu pour la première fois
print("Bienvenue au Julito's BlackJack !")
while True:  # Boucle infinie
    jouer = input("Jouer ? (o/n) ")  # Demande à l'utilisateur s'il veut jouer
    if jouer == "o":  # Si l'utilisateur répond "o"
        jouer_blackjack()  # Appelle la fonction jouer_blackjack
        break  # Sort de la boucle while
    elif jouer == "n":  # Si l'utilisateur répond "n"
        break  # Sort de la boucle while
    else:  # Si l'utilisateur répond autre chose
        print("Réponse invalide.")  # Affiche un message d'erreur

# Demander si le joueur veut jouer à nouveau
while True:  # Boucle infinie
    rejouer = input("Voulez-vous jouer à nouveau? (o/n) ")  # Demande à l'utilisateur s'il veut rejouer
    if rejouer == "o":  # Si l'utilisateur répond "o"
        jouer_blackjack()  # Appelle la fonction jouer_blackjack
    elif rejouer == "n":  # Si l'utilisateur répond "n"
        print("Merci d'avoir joué!")  # Affiche un message de remerciement
        break  # Sort de la boucle while
    else:  # Si l'utilisateur répond autre chose
        print("Veuillez entrer 'o' pour oui ou 'n' pour non.")  # Affiche un message d'erreur
        continue  # continue la boucle while s'il y a une réponse invalide