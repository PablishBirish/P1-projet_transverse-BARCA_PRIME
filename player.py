import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health =100
        self.speed =10
        self.image=pygame.image.load('assets/v2.png')
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
