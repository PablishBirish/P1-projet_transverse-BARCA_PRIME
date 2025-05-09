import pygame, random
WIDTH = 1280
HEIGHT = 720
BLUE = (0, 0, 255)
def perso():
    perso_image = pygame.image.load("assets/Personnage_2.png")
    perso_image = pygame.transform.scale(perso_image, (200, 200))
    return perso_image
#av
#1