import pygame, random
WIDTH = 1280
HEIGHT = 720
BLUE = (0, 0, 255)
class perso:
    def __init__(self):
        pygame.init()
        perso_image = pygame.image.load("assets/Personnage_2.png")
        obstacle_image = pygame.image.load(perso_image)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        if perso_image:
            obstacle_image = pygame.transform.scale(obstacle_image, (200, 200))

    def move_perso(self):

