import pygame
import sys

pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ashgoat")

# Charger l'image de fond
background = pygame.image.load('assets/fond.png')


from Game import Game

game = Game()
running = True

while running:
    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)

    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

