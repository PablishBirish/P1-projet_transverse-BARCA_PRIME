import pygame, sys, chute_libre, random, player, Equation_Trajectoire, time
from button import Button

# Initialisation de pygame et du mixer pour la musique
pygame.init()
pygame.mixer.init()

# Définition des dimensions de la fenêtre
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Menu")

# Chargement des images de fond
BG = pygame.image.load("assets/fond.png")
fond_busan = pygame.image.load("assets/fondbusan2.webp")
fond_moon = pygame.image.load("assets/fond moon.png").convert()
fond_moon = pygame.transform.scale(fond_moon, (WIDTH, HEIGHT))
fond_option = pygame.image.load("assets/fond_option.jpg")

# Fichiers audio pour les musiques de fond
musique_menu = "assets/BroForce.mp3"
musique_busan = "assets/Corail.mp3"

# Fonction pour récupérer une police personnalisée, ou une par défaut si erreur
def get_font(size):
    try:
        return pygame.font.Font("assets/font.ttf", size)
    except:
        return pygame.font.SysFont("Arial", size)

# Fonction pour jouer une musique en boucle
def jouer_musique(fichier):
    pygame.mixer.music.load(fichier)
    pygame.mixer.music.play(-1)

# Écran de jeu principal (Busan ou Moon)
def show_black_screen(destination):
    running = True
    start_time = pygame.time.get_ticks()
    score_time = pygame.time.get_ticks()
    obs = {}  # Dictionnaire pour stocker les obstacles
    first_run = True
    dx, dy = WIDTH // 2, HEIGHT // 4  # Position initiale du joueur
    score = 0

    while running:
        current_time = pygame.time.get_ticks()

        # Mise à jour du score toutes les 2 secondes
        if current_time - score_time > 2000:
            score += 1
            score_time = current_time

        # Initialisation spécifique selon la destination choisie
        if destination == "Busan" and first_run:
            dx, dy = Equation_Trajectoire.lancement_joueur()
            gravite = 10
            name_obstacle = ["assets/obstacle1.png", "assets/obstacle2.png"]
            fond = fond_busan
            jouer_musique(musique_busan)
        elif destination == "Moon" and first_run:
            dx, dy = Equation_Trajectoire.lancement_joueur()
            gravite = 5
            name_obstacle = ["assets/obstacle_lune_1.png"]
            fond = fond_moon
            SCREEN.blit(fond_moon, (0, 0))

        SCREEN.blit(fond, (0, 0))
        perso = player.perso()
        SCREEN.blit(perso, (dx, dy))

        # Ajout d’un nouvel obstacle toutes les 0.5 secondes
        if current_time - start_time > 500 or first_run:
            obs[f"obstacle_{len(obs)}"] = [chute_libre.display_obstacle(random.choice(name_obstacle)), 720]
            first_run = False
            start_time = current_time

        # Nettoyage et réindexation des obstacles pour éviter qu'ils ne sortent de l’écran
        obs = {k: v for k, v in obs.items() if v[1] > -200}
        obs = {f"obstacle_{i}": v for i, v in enumerate(obs.values())}

        # Affichage et gestion des collisions
        for i in range(len(obs)):
            obstacle, pos_x = obs[f"obstacle_{i}"][0]
            pos_y = obs[f"obstacle_{i}"][1]
            SCREEN.blit(obstacle, (pos_x, pos_y))
            obs[f"obstacle_{i}"][1] -= gravite

            # Détection de collision via les masques
            perso_mask = pygame.mask.from_surface(perso)
            obstacle_mask = pygame.mask.from_surface(obstacle)
            offset = (pos_x - dx, pos_y - dy)
            if perso_mask.overlap(obstacle_mask, offset):
                pygame.display.update()
                return  # Fin du jeu en cas de collision

        # Contrôles du joueur
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            dx += 10
        elif keys[pygame.K_q]:
            dx -= 10
        elif keys[pygame.K_z]:
            dy -= 2
        elif keys[pygame.K_s]:
            dy += 2

        # Affichage du score en haut à gauche
        score_text = get_font(36).render(f"Score: {score}", True, "Black")
        SCREEN.blit(score_text, (20, 20))

        pygame.display.update()
        clock.tick(60)

        # Gestion des événements (fermeture ou retour au menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                return

# Écran des options
def options():
    while True:
        SCREEN.blit(fond_option, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        # Affichage des instructions
        texts = [
            "If you wanna go right press D",
            "If you wanna go left press Q",
            "You gonna fall automatically",
            "Dodge everything and GL"
        ]
        for i, text in enumerate(texts):
            OPTIONS_TEXT = get_font(30).render(text, True, "White")
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_TEXT.get_rect(center=(640, 100 + i * 50)))

        # Bouton de retour
        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                return

        pygame.display.update()

# Choix entre les différentes destinations
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Où veux-tu aller ?", True, "White")
        SCREEN.blit(PLAY_TEXT, PLAY_TEXT.get_rect(center=(640, 150)))

        # Création des boutons pour les destinations
        buttons = [
            Button(image=None, pos=(640, 300), text_input="BUSAN", font=get_font(45), base_color="White",
                   hovering_color="Green"),
            Button(image=None, pos=(640, 400), text_input="MOON", font=get_font(45), base_color="White",
                   hovering_color="Green"),
            Button(image=None, pos=(640, 500), text_input="BACK", font=get_font(45), base_color="White",
                   hovering_color="Green")
        ]

        for button in buttons:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].checkForInput(PLAY_MOUSE_POS):
                    show_black_screen("Busan")
                if buttons[1].checkForInput(PLAY_MOUSE_POS):
                    show_black_screen("Moon")
                if buttons[2].checkForInput(PLAY_MOUSE_POS):
                    return

        pygame.display.update()

# Menu principal du jeu
def main_menu():
    while True:
        jouer_musique(musique_menu)
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        SCREEN.blit(MENU_TEXT, MENU_TEXT.get_rect(center=(640, 100)))

        # Création des boutons du menu principal
        buttons = [
            Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), text_input="PLAY",
                   font=get_font(75), base_color="#d7fcd4", hovering_color="White"),
            Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), text_input="OPTIONS",
                   font=get_font(75), base_color="#d7fcd4", hovering_color="White"),
            Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT",
                   font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ]

        for button in buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].checkForInput(MENU_MOUSE_POS):
                    play()
                if buttons[1].checkForInput(MENU_MOUSE_POS):
                    options()
                if buttons[2].checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Lancement du menu principal
main_menu()
pygame.quit()
