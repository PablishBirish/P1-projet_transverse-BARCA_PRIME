#Musique de jeu
import pygame
pygame.mixer.init()
#def set_mode(size=00, flags=0, display=0) :
  #  screen.fill((0, 0, 0))

etat = "menu"
musique_menu = "assets/BroForce.mp3"
pygame.mixer.music.load(musique_menu)
musique_jeu = "assets/Corail.mp3"

def jouer_musique(fichier):
    pygame.mixer.music.load(fichier)
    pygame.mixer.music.play(-1)  # -1 = boucle infinie

jouer_musique(musique_menu)

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and etat == "menu":
                # Passage au jeu
                etat = "jeu"
                jouer_musique(musique_jeu)


#avv