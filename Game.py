# test test test te

import pygame
from player player

class Game :
    def __init__ (self):
        # Initialisation des variables
        screen = pygame.display.set_mode((1280, 720))

        # Mise en place de la fenêtre
        pygame.display.set_mode((1773, 1072))  # On délimite la taille de la fenêtre
        pygame.display.set_caption("Projet Transverse - V1")  # On donne un nom à la fenêtre
        self.player = Player()
        self.pressed = {
            "droite": True,
            "gauche": False,}

    def run (self):
        running = True  # Cette variable contient l'état de fonctionnement du jeu ('True' s'il tourne, 'False' s'il ne tourne pas)
        while running:  # Cette boucle fera tourner le jeu tant que la variable 'running' est égal à 'True'
            for event in pygame.event.get():  # On récupère la liste des évènements actifs
                if event.type == pygame.QUIT:  # On récupère et vérifie le type d'évènement
                    running = False  # Si le joueur tente de fermer la fenêtre (le type d'évènement est le fait de quitter), le programme sort de la boucle while



#avv
#1