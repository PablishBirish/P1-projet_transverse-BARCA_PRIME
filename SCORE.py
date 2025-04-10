# SCORE
import pygame
import sys

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Police
police = pygame.font.SysFont(None, 48)

# Variables
timer_score = 0  # en dixièmes de secondes
game_over = False
clock = pygame.time.Clock()
temps_accumule = 0

# Vitesse du compteur : toutes les 100 ms → 10 points/sec
vitesse_timer = 100  # en millisecondes

# Boucle principale
running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Simule une fin de jeu avec une touche (exemple : barre espace)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_over = True

    if not game_over:
        temps_accumule += dt
        if temps_accumule >= vitesse_timer:
            timer_score += 1
            temps_accumule = 0
            print(f"Temps (score) actuel : {timer_score:05d}")

    # Affichage du score
    fenetre.fill(NOIR)  # Nettoie la fenêtre pour chaque frame

    if not game_over:
        texte_score = police.render(f"Score : {timer_score:05d}", True, BLANC)
        fenetre.blit(texte_score, (20, 20))  # Affiche le score en haut à gauche
    else:
        texte_fin = police.render(f"Game Over - Temps final : {timer_score:05d}", True, BLANC)
        fenetre.blit(texte_fin, (largeur // 2 - 200, hauteur // 2))  # Affiche "Game Over" au centre

    pygame.display.flip()  # Met à jour l'écran

sys.exit()

