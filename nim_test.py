import random
 
class JeuNim:    # Ici, on utilise une class pour faciliter l'utilisation et l'organistion du jeu

    def __init__(self, n, m):
        self.n = n   # Nombre d'allumette
        self.m = m   # Nombre de coups
 
    def etat(self):
        return self.n   # Retourne le nombre d'allumette
    
    def nbr_coup(self):
        return self.m   # Retourne le nombre de coup
 
    def estVide(self, etat):    # Vérifie si le sac d'allumette est vide
        if etat == 0:
            return True
        else:
            return False
 
    # Cette fonction fixe les conditions de victoire. Si l'on inverse float("+inf") et float("-inf"), on remarquera que l'oridnateur cherchera à perdre
    def condition_victoire(self, etat, joueur):
        if etat == 0:
            if joueur == 1:
                return float('+inf')
            else:
                return float('-inf')
            
    # Cette fonction fixe le nombre de bâtons retirables
    def actions(self, etat, m):
        if etat >= m:
            return [i for i in range(1,m+1)]
        return range(1, etat + 1)
    
    # Cette fonction nous donne le successeur
    def enfant(self, etat, retire):
        if retire > etat:
            return 0
        return etat - retire

# Minmax
def minmax(jeu, etat, m, joueur):

    # Cette fonction est une fonction récurssive qui va vérifier quel est le meilleur choix en fonction du score
    def verification(etat, m, joueur):
        if jeu.estVide(etat) == True:
            return (jeu.condition_victoire(etat, joueur), None)
        if (etat, joueur) in cache:
            return cache[(etat, joueur)]
        choix = [(verification(jeu.enfant(etat, retire),m, -1 * joueur)[0], retire) for retire in jeu.actions(etat,m)]
        if joueur == +1:
            val = max(choix)
        else:
            val = min(choix)
        cache[(etat, joueur)] = val
        return val
 
    valeur, retire = verification(etat, m, joueur)
    return (valeur, retire)

# On initialise d'abord nos valeurs
cache = {}
allumettes = int(input("Avec combien d'allumettes voulez vous jouer? "))
coups = int(input("Avec combien de coups voulez vous jouer? "))
jeu = JeuNim(allumettes,coups)
etat = jeu.etat()
m = jeu.nbr_coup()
joueur_actuel = random.choice([1, -1])

print("Le jeu commence")

# On joue tant qu'il reste des allumettes
while etat > 0:
    retire = 0
    print("Il y a ", etat, "allumettes")
    while (retire not in range(1,jeu.nbr_coup()+1)) and etat - retire >= 0:
        retire = int(input("Choisissez le nombre d'allumettes à retirer : "))
    
    # On vérifie si on peut retirer les allumettes
    if retire <= etat:
        etat -= retire
        print("Il reste ", etat, "allumettes")

        # On vérifie si l'ordinateur gagne
        if etat == 0:
            print("Ahahahahahahahahahahahahahahah le gros nul, vous avez perdu !")
            break   # break si jeu fini
        valeur, action = minmax(jeu, etat, m, joueur_actuel)
        etat -= action
        print("L'ordinateur a retiré", action, " allumettes")
        if etat == 0:
            print("Félicitations ! Vous avez gagné !")
    else:
        print("Vous deveez retirer moins d'alumettes")
 