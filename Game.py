import pygame
from player import Player

class Game:
    def __init__(self):
        # Définition de la fenêtre du jeu
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Projet Transverse - V1")

        # Initialisation du joueur
        self.player = Player()

        self.pressed = {
            "droite": False,
            "gauche": False
        }

    def run(self):
        running = True

        while running:
            self.screen.fill((0, 0, 0))

            # Afficher le joueur
            self.screen.blit(self.player.image, self.player.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.pressed["droite"] = True
                    if event.key == pygame.K_q:
                        self.pressed["gauche"] = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.pressed["droite"] = False
                    if event.key == pygame.K_q:
                        self.pressed["gauche"] = False

pygame.quit()





