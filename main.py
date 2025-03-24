import pygame
import sys
import subprocess
from button import Button


pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

# Charger l’image de fond
BG = pygame.image.load("assets/fond.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def launch_game(destination):
    """Lancer le jeu dans une nouvelle fenêtre avec le bon niveau (Busan ou Moon)."""
    if destination == "Busan":
        subprocess.Popen(["python", "game1.py"])  # Ouvre game1.py
    elif destination == "Moon":
        subprocess.Popen(["python", "game2.py"])  # Ouvre game2.py (à créer si nécessaire)

        BUSAN_BUTTON = Button(image=None, pos=(640, 300),
                              text_input="BUSAN", font=get_font(45), base_color="White", hovering_color="Green")

        LUNE_BUTTON = Button(image=None, pos=(640, 400),
                             text_input="LA LUNE", font=get_font(45), base_color="White", hovering_color="Green")



def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(30).render("If you wanna go right press D", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT1 = get_font(30).render("If you wanna go left press Q", True, "Black")
        OPTIONS_RECT1 = OPTIONS_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(OPTIONS_TEXT1, OPTIONS_RECT1)
        OPTIONS_TEXT3 = get_font(30).render("You gonna fall automaticly", True, "Black")
        OPTIONS_RECT3 = OPTIONS_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)
        OPTIONS_TEXT4 = get_font(30).render("Dodge everything", True, "Black")
        OPTIONS_RECT4 = OPTIONS_TEXT.get_rect(center=(840, 250))
        SCREEN.blit(OPTIONS_TEXT4, OPTIONS_RECT4)

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
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

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

def play():
    """Affiche l'écran de sélection des niveaux (Busan / Moon)."""
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Où veux-tu aller ?", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

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
                    launch_game("Busan")
                if MOON_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    launch_game("Moon")
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
main_menu()





pygame.quit()

