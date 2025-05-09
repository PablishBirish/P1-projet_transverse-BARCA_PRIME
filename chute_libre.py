import pygame, random
WIDTH = 1280
HEIGHT = 720
BLUE = (0, 0, 255)


class Player:
    """
    Représente le personnage principal (joueur) affecté par la gravité.

    Attributs :
    - image : surface pygame représentant le joueur.
    - rect : rectangle de collision du joueur.
    - velocity_y : vitesse verticale du joueur.
    - gravity : intensité de la gravité.
    - max_speed : vitesse maximale de chute.
    - on_ground : booléen indiquant si le joueur touche le sol.
    """

    def __init__(self):
        """Initialise le joueur avec une position, une image et des paramètres de physique."""
        self.image = pygame.Surface((50, 50))  # Crée un carré de 50x50 px
        self.image.fill(BLUE)  # Colore le joueur en bleu
        self.rect = self.image.get_rect(center=(WIDTH // 2, 50))  # Place au centre en haut de l'écran
        self.velocity_y = 0  # Vitesse verticale initiale nulle
        self.gravity = 0.5   # Gravité qui agit vers le bas
        self.max_speed = 7   # Vitesse limite de chute pour éviter qu'il ne tombe trop vite
        self.on_ground = False  # Le joueur commence en l'air

    def apply_gravity(self):
        """
        Applique la gravité sur le joueur si celui-ci n’est pas au sol.
        Augmente progressivement la vitesse de chute jusqu’à une limite.
        """
        if not self.on_ground:
            self.velocity_y += self.gravity  # Accélère vers le bas
            if self.velocity_y > self.max_speed:
                self.velocity_y = self.max_speed  # Empêche de dépasser la vitesse maximale
            self.rect.y += self.velocity_y  # Applique le déplacement vertical

    def check_ground_collision(self):
        """
        Vérifie si le joueur touche le sol.
        Si oui, le joueur est arrêté et repositionné exactement sur le sol.
        """
        ground_y = HEIGHT - 50  # Position verticale du sol (en pixels)
        if self.rect.bottom >= ground_y:
            self.rect.bottom = ground_y  # Replace le joueur au bon endroit
            self.velocity_y = 0          # Annule la vitesse pour l’arrêter
            self.on_ground = True        # Marque qu’il est au sol
        else:
            self.on_ground = False       # Sinon il est en l'air

    def update(self):
        """
        Met à jour la position du joueur en appliquant la gravité et en vérifiant les collisions.
        À appeler à chaque frame.
        """
        self.apply_gravity()
        self.check_ground_collision()

    def draw(self, screen):
        """
        Affiche le joueur à l'écran à sa position actuelle.
        - screen : la surface Pygame sur laquelle dessiner.
        """
        screen.blit(self.image, self.rect)

def display_obstacle(img):
    """
    Charge et redimensionne un obstacle selon son type, puis lui attribue une position horizontale aléatoire.

    Paramètre :
    - img : chemin vers l’image de l’obstacle (fichier PNG).

    Retourne :
    - obstacle_image : surface pygame de l’obstacle redimensionné.
    - pos_x_obstacle : position x aléatoire pour placer l’obstacle à l’écran.
    """
    obstacle_image = pygame.image.load(img)  # Charge l'image

    if img == "assets/obstacle1.png":
        pos_x_obstacle = random.randint(0, 1280 - 200)  # Génère une position aléatoire
        obstacle_image = pygame.transform.scale(obstacle_image, (200, 200))  # Redimensionne à 200x200
    elif img == "assets/obstacle2.png":
        pos_x_obstacle = random.randint(0, 1280 - 100)
        obstacle_image = pygame.transform.scale(obstacle_image, (100, 100))
    elif img == "assets/obstacle_lune_1.png":
        pos_x_obstacle = random.randint(0, 1280 - 100)
        obstacle_image = pygame.transform.scale(obstacle_image, (150, 150))

    return obstacle_image, pos_x_obstacle  # Retourne l’image + sa position horizontale
