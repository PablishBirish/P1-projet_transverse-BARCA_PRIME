import pygame, sys, chute_libre, random
from button import Button

pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Menu")

# Chargement des images
BG = pygame.image.load("assets/fond.png")
fond_busan = pygame.image.load("assets/fondbusan2.webp")  # Image de Busan


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def show_black_screen(destination):
    """Affiche l'écran correspondant à la destination."""
    running = True
    start_time = pygame.time.get_ticks()
    obs = {}
    first_run = True
    while running:
        if destination == "Busan":
            gravite = 15
            name_obstacle = ["assets/obstacle1.png", "assets/obstacle2.png"]
            SCREEN.blit(fond_busan, (0, 0))  # Affiche l'image de Busan
        else:
            gravite = 5
            name_obstacle = ["assets/obstacle_lune_1.png"]
            SCREEN.fill("black")  # Affiche un écran noir pour les autres destinations

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

        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(obs)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Retour au menu principal avec Échap
                    return


def options():
    """Affiche les options du jeu."""
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(30).render("If you wanna go right press D", True, "Black")
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_TEXT.get_rect(center=(640, 100)))

        OPTIONS_TEXT1 = get_font(30).render("If you wanna go left press Q", True, "Black")
        SCREEN.blit(OPTIONS_TEXT1, OPTIONS_TEXT1.get_rect(center=(640, 150)))

        OPTIONS_TEXT3 = get_font(30).render("You gonna fall automatically", True, "Black")
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_TEXT3.get_rect(center=(640, 200)))

        OPTIONS_TEXT4 = get_font(30).render("Dodge everything and GL", True, "Black")
        SCREEN.blit(OPTIONS_TEXT4, OPTIONS_TEXT4.get_rect(center=(640, 250)))

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

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
        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Où veux-tu aller ?", True, "White")
        SCREEN.blit(PLAY_TEXT, PLAY_TEXT.get_rect(center=(640, 150)))

        # Bouton Busan
        BUSAN_BUTTON = Button(image=None, pos=(640, 300),
                              text_input="BUSAN", font=get_font(45), base_color="White", hovering_color="Green")
        BUSAN_BUTTON.changeColor(PLAY_MOUSE_POS)
        BUSAN_BUTTON.update(SCREEN)

        # Bouton Moon
        MOON_BUTTON = Button(image=None, pos=(640, 400),
                             text_input="MOON", font=get_font(45), base_color="White", hovering_color="Green")
        MOON_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOON_BUTTON.update(SCREEN)

        # Bouton Retour
        PLAY_BACK = Button(image=None, pos=(640, 500),
                           text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUSAN_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    show_black_screen("Busan")  # Afficher l’image de Busan
                if MOON_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    show_black_screen("Moon")  # Afficher un écran noir
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    return

        pygame.display.update()


def main_menu():
    """Affiche le menu principal."""
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        SCREEN.blit(MENU_TEXT, MENU_TEXT.get_rect(center=(640, 100)))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


# Lancer le menu
main_menu()

pygame.quit()



