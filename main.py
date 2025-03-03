import pygame

# Initialisation des variables
running = True          # Cette variable contient l'état de fonctionnement du jeu ('True' s'il tourne, 'False' s'il ne tourne pas)
screen = pygame.display.set_mode((1280, 720))

# Mise en place de la fenêtre
pygame.display.set_mode((800, 600))         # On délimite la taille de la fenêtre
pygame.display.set_caption("Projet Transverse - V1")            # On donne un nom à la fenêtre

while running :             # Cette boucle fera tourner le jeu tant que la variable 'running' est égal à 'True'
    for event in pygame.event.get():                # On récupère la liste des évènements actifs
        if event.type == pygame.QUIT :          # On récupère et vérifie le type d'évènement
            running = False             # Si le joueur tente de fermer la fenêtre (le type d'évènement est le fait de quitter), le programme sort de la boucle while
pygame.quit()