import pygame, random
WIDTH = 1280
HEIGHT = 720
BLUE = (0, 0, 255)



class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, 50))
        self.velocity_y = 0  # Vitesse verticale
        self.gravity = 0.5   # Force de gravité
        self.max_speed = 7  # Vitesse maximale en chute libre
        self.on_ground = False

    def apply_gravity(self):
        if not self.on_ground:
            self.velocity_y += self.gravity
            if self.velocity_y > self.max_speed:
                self.velocity_y = self.max_speed  # Limite la vitesse de chute
            self.rect.y += self.velocity_y

    def check_ground_collision(self):
        ground_y = HEIGHT - 50  # Position du sol
        if self.rect.bottom >= ground_y:
            self.rect.bottom = ground_y
            self.velocity_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def update(self):
        self.apply_gravity()



        self.check_ground_collision()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def display_obstacle(img):
    """ Charge, redimensionne et place un obstacle à une position x aléatoire """
    obstacle_image = pygame.image.load(img)
    if img == "assets/obstacle1.png":
        pos_x_obstacle = random.randint(0, 1280 - 200)
        obstacle_image = pygame.transform.scale(obstacle_image, (200, 200))  # Redimensionner avant blit
    elif img == "assets/obstacle2.png":
        pos_x_obstacle = random.randint(0, 1280 - 100)
        obstacle_image = pygame.transform.scale(obstacle_image, (100, 100))
    elif img == "assets/obstacle_lune_1.png":
        pos_x_obstacle = random.randint(0, 1280 - 100)
        obstacle_image = pygame.transform.scale(obstacle_image, (150, 150))
    return obstacle_image, pos_x_obstacle  # Retourner l'image et sa position
