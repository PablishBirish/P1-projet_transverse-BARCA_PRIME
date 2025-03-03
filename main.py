import pygame

# Initialisation des variables
running = True          # Cette variable contient l'état de fonctionnement du jeu ('True' s'il tourne, 'False' s'il ne tourne pas)
screen = pygame.display.set_mode((1280, 720))

# Mise en place de la fenêtre
pygame.display.set_mode((800, 600))         # On délimite la taille de la fenêtre
pygame.display.set_caption("Projet Transverse - V1")            # On donne un nom à la fenêtre