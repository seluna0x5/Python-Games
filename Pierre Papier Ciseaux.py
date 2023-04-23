import random
manches = int(input("Combien de manches voulez-vous jouer ? "))
score_joueur = 0
score_ordi = 0
rounds = 0
options = ["pierre", "papier", "ciseaux"]
while rounds<manches :
    choix_joueur = input("Que jouez vous ? Tapez 'pierre', 'papier' ou 'ciseaux'")
    if choix_joueur not in options:
        input("Choix invalide ! tapez entrer")
    else :     
        choix_ordi = random.choice(options)
        rounds += 1
        if choix_joueur == choix_ordi:
            print("Égalité.")
        elif choix_joueur == "pierre" and choix_ordi == "ciseaux" \
        or choix_joueur == "papier" and choix_ordi == "pierre" \
        or choix_joueur == "ciseaux" and choix_ordi == "papier":
            print("Vous remportez la manche,", choix_joueur, "bat" , choix_ordi)
            score_joueur += 1
        elif choix_joueur == "ciseaux" and choix_ordi == "pierre" \
        or choix_joueur == "pierre" and choix_ordi == "papier" \
        or choix_joueur == "papier" and choix_ordi == "ciseaux":
            print("L'ordinateur gagne la manche," , choix_ordi, "bat" , choix_joueur)
            score_ordi += 1
if score_joueur > score_ordi :
    print("Vous avez gagné la partie !")
elif score_joueur < score_ordi 	:
    print("L'ordinateur gagne :(")
else :
    print("Égalité! Relancez le script pour rejouer")