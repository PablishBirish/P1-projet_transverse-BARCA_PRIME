import pygame
pygame.init()
from game import Game




pygame.display.set_caption("Ashgoat")
screen =   pygame.display.set_mode((960,540 ))
background = pygame.image.load('assets/fond.png')
game = Game()
running = True

while running:

    screen.blit(background,(0,-200  ))
    screen.blit(game.player.image, game.player.rect)

    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()
    print(game.player.rect.x)
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
