

"""
Permet de faire les déplacements de droite a gauche  (q,d) jdjdjd
"""

import pygame
pygame.init()
running = True
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health =100
        self.speed =2
        self.image=pygame.image.load('assets/busanperso2.png')
        self.attack = 10
        self.maxhealth = 100
        self.rect = self.image.get_rect()
        self.rect.x = 640
        width, height = self.image.get_size()
        new_size = (width * 8, height * 8)




    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 720:
            self.rect.y = 720
class Game :
    def __init__ (self):


        self.player = Player()
        self.pressed = {
            "droite": True,
            "gauche": False,}


game = Game()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))



background = pygame.image.load("assets/fondbusan2.webp")


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
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
#avv
#vv