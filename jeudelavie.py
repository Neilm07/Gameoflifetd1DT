import numpy as np
import time
import os

def afficher_grille(grille):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran pour afficher la grille proprement
    for ligne in grille:
        print(' '.join(['□' if cellule == 0 else '■' for cellule in ligne]))

def voisinage(grille, x, y):
    """Calcule le nombre de voisins vivants d'une cellule."""
    voisins = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Ignorer la cellule elle-même
            voisins += grille[(x + i) % grille.shape[0], (y + j) % grille.shape[1]]  # Gestion des bords (tore)
    return voisins

def generation_suivante(grille):
    """Crée une nouvelle grille pour la génération suivante."""
    nouvelle_grille = np.zeros(grille.shape, dtype=int)
    for x in range(grille.shape[0]):
        for y in range(grille.shape[1]):
            voisins = voisinage(grille, x, y)
            if grille[x, y] == 1:  # Cellule vivante
                if voisins in [2, 3]:
                    nouvelle_grille[x, y] = 1  # Survit
            else:  # Cellule morte
                if voisins == 3:
                    nouvelle_grille[x, y] = 1  # Naît
    return nouvelle_grille

def jeu_de_la_vie(taille=10, iterations=100, vitesse=0.5):
    """Exécute le Jeu de la Vie."""
    # Initialiser une grille aléatoire
    grille = np.random.choice([0, 1], size=(taille, taille))

    for _ in range(iterations):
        afficher_grille(grille)
        grille = generation_suivante(grille)
        time.sleep(vitesse)

# Lancer le jeu
if __name__ == "__main__":
    jeu_de_la_vie(taille=20, iterations=200, vitesse=0.3)
