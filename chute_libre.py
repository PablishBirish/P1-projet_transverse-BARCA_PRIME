import pygame
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, 50))
        self.velocity_y = 0  # Vitesse verticale
        self.gravity = 0.5   # Force de gravité
        self.max_speed = 10  # Vitesse maximale en chute libre
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