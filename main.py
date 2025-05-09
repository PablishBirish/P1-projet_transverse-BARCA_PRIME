import pygame, sys, chute_libre, random, player, Equation_Trajectoire
from button import Button

# permet initialiser
pygame.init()
pygame.mixer.init()
# Paramètres de la fenêtre
WIDTH, HEIGHT = 1280, 720 # dededede
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Menu")

# Chargement des images
BG = pygame.image.load("assets/fond.png")
fond_busan = pygame.image.load("assets/fondbusan2.webp")  # Image de Busan
fond_moon = pygame.image.load("assets/fond moon.png").convert()
fond_moon = pygame.transform.scale(fond_moon, (WIDTH, HEIGHT))  # Image de la Lune
fond_option = pygame.image.load("assets/fond_option.jpg")  # Image pour les options

# chargement des musiques musique_menu = "assets/BroForce.mp3"
musique_menu = "assets/BroForce.mp3"
musique_busan = "assets/Corail.mp3"


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def jouer_musique(fichier):
    """Joue la musique en boucle."""
    pygame.mixer.music.load(fichier)
    pygame.mixer.music.play(-1)  # lance musique à l'infini


def show_black_screen(destination):
    """Affiche l'écran correspondant à la destination."""
    running = True
    start_time = pygame.time.get_ticks()
    obs = {}
    first_run = True
    dx, dy = WIDTH // 2, HEIGHT // 4

    while running:
        if destination == "Busan" and first_run:
            dx, dy = Equation_Trajectoire.lancement_joueur()
            gravite = 10
            name_obstacle = ["assets/obstacle1.png", "assets/obstacle2.png"]
            fond = fond_busan  # Affiche l'image de Busan
            jouer_musique(musique_busan)
        elif destination == "Moon" and first_run:
            dx, dy = Equation_Trajectoire.lancement_joueur()
            gravite = 5
            name_obstacle = ["assets/obstacle_lune_1.png"]
            fond = fond_moon  # Affiche l'image de la Lune
            SCREEN.blit(fond_moon, (0, 0))  # fond de la lune

        SCREEN.blit(fond, (0, 0))
        perso = player.perso()
        SCREEN.blit(perso, (dx, dy))

        current_time = pygame.time.get_ticks()
        if current_time - start_time > 500 or first_run:
            obs[f"obstacle_{len(obs)}"] = [chute_libre.display_obstacle(random.choice(name_obstacle)), 720]
            first_run = False
            start_time = current_time

        avion_trop_haut = [key for key in obs if obs[key][1] <= -200]
        for key in avion_trop_haut:
            del obs[key]
        obs = {f"obstacle_{i}": v for i, v in enumerate(obs.values())}
        for i in range(len(obs)):
            obstacle, pos_x = obs[f"obstacle_{i}"][0]
            pos_y = obs[f"obstacle_{i}"][1]
            SCREEN.blit(obstacle, (pos_x, pos_y))
            obs[f"obstacle_{i}"][1] -= gravite
            perso_mask = pygame.mask.from_surface(perso)
            obstacle_mask = pygame.mask.from_surface(obstacle)

            offset = (pos_x - dx, pos_y - dy)
            if perso_mask.overlap(obstacle_mask, offset):
                pygame.display.update()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            dx += 10
        elif keys[pygame.K_q]:
            dx -= 10
        elif keys[pygame.K_z]:
            dy -= 2
        elif keys[pygame.K_s]:
            dy += 2
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    return


def options():
    """Affiche les options du jeu avec un fond d'écran."""
    while True:

        SCREEN.blit(fond_option, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        texts = [
            "If you wanna go right press D",
            "If you wanna go left press Q",
            "You gonna fall automatically",
            "Dodge everything and GL"
        ]

        for i, text in enumerate(texts):
            OPTIONS_TEXT = get_font(30).render(text, True, "White")
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_TEXT.get_rect(center=(640, 100 + i * 50)))

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return

        pygame.display.update()


def play():
    """Affiche l'écran de sélection des niveaux (Busan / Moon)."""
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Où veux-tu aller ?", True, "White")
        SCREEN.blit(PLAY_TEXT, PLAY_TEXT.get_rect(center=(640, 150)))

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


def main_menu():
    """Affiche le menu principal."""
    while True:
        jouer_musique(musique_menu)
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        SCREEN.blit(MENU_TEXT, MENU_TEXT.get_rect(center=(640, 100)))

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


# Lancer le menu
main_menu()
pygame.quit()
# av