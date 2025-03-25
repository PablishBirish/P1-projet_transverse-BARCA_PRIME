import pygame

class Obstacle(pygame.sprite.Sprite):
        def __init__(self, image_path, x, y):
            super().__init__()
            self.image = pygame.image.load(image_path).convert_alpha()  # Charger l'image
            self.rect = self.image.get_rect(topleft=(x, y))  # Définir la position et la hitbox

obstacle1 = Obstacle("assets/obstacle1.png", 800, 400)  # Position statique
obstacle2 = Obstacle("assets/obstacle2.png", 1000, 300)  # Position statique

# Ajouter les obstacles dans un groupe de sprites pour les gérer facilement
obstacles = pygame.sprite.Group()
obstacles.add(obstacle1, obstacle2)
