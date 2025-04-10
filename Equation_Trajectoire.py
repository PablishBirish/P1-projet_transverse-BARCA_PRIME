import pygame
import math

# Initialisation de PyGame et de la fenêtre de jeu
pygame.init()
WIDTH, HEIGHT = 1100, 800  # Dimensions de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Equation trajectoire test")
clock = pygame.time.Clock()

# Constantes physiques qui serviront pour le calcul de la trajectoire
g = 9.81  # constante gravitationnelle
m = 80  # masse en kg
k = 0.5  # coefficient de frottement

# Paramètres initiaux du jeu
angle_deg = 45  # angle de tir 
power = 15  # m/s
launched = False  # Vrai ou faux si le parachutiste est lancé ou non
camera_x = 0  # Décalage horizontal de la caméra
parachute_deployed = False  # Vrai ou faux si le parachute est déployé ou non

# Position initiale du parachutiste (en pixels)
x, y = 100, HEIGHT - 100
vx, vy = 0, 0   # paramètres initiales de la vitesse sur les deux axes

# Couleurs (tempo)
WHITE = (255, 255, 255)
RED = (200, 50, 50)
BLUE = (50, 100, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Police et taille d'écriture (font, 24 pixels)
font = pygame.font.SysFont(None, 24)

# Dessin de la flèche qui représente la puissance du tir + son angle
def draw_arrow(surface, x, y, angle_deg, power, camera_x):
    angle_rad = math.radians(angle_deg)  # convertie l'angle en radians, nécessaire pour utiliser ensuite math.cos(angle)
    length = power * 10  # Multipliée par 10 pour être visible à l'écran
    end_x = x + length * math.cos(angle_rad)  # Fin de la flèche en fonction de : longueur + origine + angle
    end_y = y - length * math.sin(angle_rad)  # Fin de la flèche en fonction de : longueur + origine + angle
    pygame.draw.line(surface, RED, (x - camera_x, y), (end_x - camera_x, end_y), 4)  # Dessine un trait rouge entre (x; y) et (end_x; end_y)

# Dessin de la jauge indicatrice de la puissance du tir
def draw_power_bar(surface, power):
    pygame.draw.rect(surface, BLACK, (50, HEIGHT - 40, 300, 20), 2)  # Dessine le contour de la jauge (un rectangle)
    pygame.draw.rect(surface, GREEN, (50, HEIGHT - 40, power / 30 * 300, 20))  # Remplie la jauge en fonction de la puissance de tir
        # On utilise une règle de 3, le maximum de puissance est 30 soit 300 pixels sur la jauge

# Met à jour régulièrement la physique du parachutiste pour recréer une chute réaliste
def update_physics(x, y, vx, vy, dt, parachute):
    # Forces (x) : frottements (2e loi de Newton)
    ax = - (k / m) * vx
    # Forces (y) : poids + frottements (2e loi de Newton)
    ay = g - (k / m) * vy
    if parachute == True :
        ax *= 5  # Amplification de la résistance de l'air sur l'axe x (à cause du parachute)
        ay *= 5  # Amplification de la résistance de l'air l'axe y (à cause du parachute)

    # Intégration
    vx += ax * dt
    vy += ay * dt
    x += vx * dt * 100  # On multiplie par 100 pour affichage
    y += vy * dt * 100

    # Évite que le parachutiste tombe en dessous du sol visible
    if y > HEIGHT - 10:  # On dit que le sol fait 10 pixels de hauteur au bas de la fenêtre
        y = HEIGHT - 10
        vy = 0  # On met la vitesse sur l'axe y (son dernier où il est en mouvement normalement) à 0 pour qu'il s'arrête
    return x, y, vx, vy


# Boucle principale
running = True
while running:
    dt = clock.tick(60) / 1000  # en secondes
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Contrôles avant lancement
    keys = pygame.key.get_pressed()
    if not launched:
        if keys[pygame.K_LEFT] and angle_deg > 0:    # Si le joueur presse la flèche directionnelle gauche
            angle_deg -= 1
        if keys[pygame.K_RIGHT] and angle_deg < 80:    # Si le joueur presse la flèche directionnelle droite
            angle_deg += 1
        if keys[pygame.K_UP] and power < 30:     # Si le joueur presse la flèche directionnelle haut
            power += 0.5
        if keys[pygame.K_DOWN] and power > 0:    # Si le joueur presse la flèche directionnelle bas
            power -= 0.5
        if keys[pygame.K_SPACE]:    # Si le joueur presse la touche espace
            angle_rad = math.radians(angle_deg)
            vx = power * math.cos(angle_rad)  # équations de la vitesse (physique)
            vy = - power * math.sin(angle_rad)  # équations de la vitesse (physique)
            launched = True   # Le parachutiste est maintenant lancé

    if launched and keys[pygame.K_p]:
        parachute_deployed = True

    # Mise à jour de la physique en temps réel
    if launched:
        x, y, vx, vy = update_physics(x, y, vx, vy, dt, parachute_deployed)  # Modifie la position du parachutiste

        # Scroll horizontal : garde la caméra centrée sur le parachutiste
        camera_x = x - WIDTH // 4
        if camera_x < 0:
            camera_x = 0  # Ne jamais décaler vers la gauche

    # Dessin de la flèche (symbolise la puissance et l'angle de tir)
    if not launched:
        draw_arrow(screen, x, y, angle_deg, power, camera_x)
        draw_power_bar(screen, power)
    pygame.draw.circle(screen, BLUE if not parachute_deployed else GREEN, (int(x - camera_x), int(y)), 10)

    # Affichage des commandes pour le joueur
    txt = font.render(f"Angle : {angle_deg}° | Vitesse : {power:.1f} m/s", True, BLACK)
    screen.blit(txt, (10, 10))
    if not launched:
        screen.blit(font.render("ESPACE pour lancer", True, BLACK), (10, 35))
    else:
        screen.blit(font.render("P pour déployer le parachute", True, BLACK), (10, 35))

    pygame.display.flip()

pygame.quit()
