# Importation de la librairie random et de la librairie datetime
import random
from datetime import datetime


# Définition de la fonction replay()
def replay():
    # Demande à l'utilisateur s'il veut rejouer
    choice = input('Voulez-vous rejouer ? (o/n) ').lower()
    # Si l'utilisateur veut rejouer
    if choice == 'o':
        # Appel de la fonction shifumi()
        shifumi()
    # Sinon
    else:
        # Affichage du message "Au revoir !"
        print('Au revoir !')


# Définition de la fonction scoreboard()
def scoreboard():
    # Ouverture du fichier score.txt en mode lecture
    with open('score.txt', 'r') as file:
        # Affichage du contenu du fichier score.txt
        print(file.read())

    replay()


# Définition de la fonction menu()
def menu():
    # Affichage du menu
    print('⌈----- Pierre, Papier, Ciseaux -----⌉')
    print('| 1. En une manche gagnantes        |')
    print('| 2. En deux manches gagnantes      |')
    print('| 3. En trois manches gagnantes     |')
    print('| 4. Statistiques                   |')
    print('⌊-----------------------------------⌋')

    # Demande à l'utilisateur de choisir une option
    choice = input('Choisissez une option: ')
    # Si l'utilisateur a choisi l'option 1
    if choice == '1':
        # Retourne 1
        return 1
    # Si l'utilisateur a choisi l'option 2
    elif choice == '2':
        # Retourne 2
        return 2
    # Si l'utilisateur a choisi l'option 3
    elif choice == '3':
        # Retourne 3
        return 3
    # Si l'utilisateur a choisi l'option 4
    elif choice == '4':
        # Appel de la fonction scoreboard()
        scoreboard()


# Définition de la fonction shifumi()
def shifumi(choice=None):
    # Définition des choix possibles
    choice = ['pierre', 'papier', 'ciseaux'] if choice is None else choice

    # Appel de la fonction menu() et stockage du résultat dans la variable win
    win = menu()
    # Initialisation du score
    score = {'player': 0, 'computer': 0}

    # Tant que le score du joueur et de l'ordinateur est inférieur au score à atteindre
    while score['player'] < win and score['computer'] < win:
        # Demande à l'utilisateur de choisir entre pierre, papier ou ciseaux
        player = input('Pierre, papier ou ciseaux ? ').lower()
        # L'ordinateur choisit aléatoirement entre pierre, papier ou ciseaux
        computer = random.choice(choice)

        # Affichage des choix du joueur et de l'ordinateur
        print(f'Joueur: {player} - Ordinateur: {computer}')

        # Si le joueur et l'ordinateur ont choisi la même chose
        if player == computer:
            # Affichage du message "Egalité"
            print('Egalité')
        # Si le joueur a choisi un élément qui bat l'élément choisi par l'ordinateur
        elif player == 'pierre' and computer == 'ciseaux' or player == 'papier' and computer == 'pierre' or player == 'ciseaux' and computer == 'papier':
            # Affichage du message "Vous avez gagné !"
            print('Vous avez gagné !')
            # Incrémentation du score du joueur
            score['player'] += 1
        # Sinon
        else:
            # Affichage du message "Vous avez perdu !"
            print('Vous avez perdu !')
            # Incrémentation du score de l'ordinateur
            score['computer'] += 1

        # Affichage du score du joueur et de l'ordinateur
        print(f'Joueur: {score["player"]} - Ordinateur: {score["computer"]}')

    # Si le score du joueur est égal au score à atteindre
    if score['player'] == win:
        # Affichage du message "Vous avez gagné la partie !"
        print('Vous avez gagné la partie !')
    # Sinon
    else:
        # Affichage du message "Vous avez perdu la partie !"
        print('Vous avez perdu la partie !')

    # Ouverture du fichier score.txt en mode écriture
    with open('score.txt', 'a') as file:
        # Écriture du score dans le fichier score.txt
        file.write(f'{input('Entrez votre nom: ')} : {score["player"]} - {score["computer"]} le {datetime.now().strftime("%d/%m/%Y")}\n')

    # Appel de la fonction replay()
    replay()

