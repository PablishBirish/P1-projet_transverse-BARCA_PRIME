# P1-projet_transverse-BIRAN-
Dans le cadre de notre projet transverse en première année à l'EFREI, nous avons l'opportunité de réaliser un jeu vidéo en 2D de A à Z en Python à l'aide du module Pygame. 

## Description du Jeu
Le joueur incarne un parachutiste, qui s’élance dans le vide depuis un hélicoptère/avion dans le but d’atteindre une cible au sol. Cependant le ciel contient des obstacles, pouvant entraîner la mort du parachutiste et donc la fin de la partie. 

Le gameplay se décompose en 2 phases principales : 
  1. **Phase de Lancée** : Le joueur a la possibilité de jauger lui même la force et l'angle du lancer, il doit bien choisir vers où s’élancer car il devra par la suite esquiver les obstacles de la zone.
       Commandes :
           - **Espace** pour lancer
           - flèches directionnelles **gauche** et **droite** pour régler la vitesse initiale (de 0 à 30m/s)
           - flèches directionnelles **haut** et **bas** pour régler l'angle de tir (0 à 80 degré)
           - **E** pour ouvrir le parachute
  3. **Phase de Descente** : Le joueur a été lancé et a ouvert son parachute, il doit à présent atteindre une cible au sol sain et sauf sous peine de Game Over.


## Fonctionnalités
### Différents monde où jouer
Le joueur aura l'opportunité de jouer sur **3 cartes/mondes** différents :
- Busan
  - Gravité classique
  - Les obstacles sont des avions et des oiseaux
- Moon
  - Gravité réduite
  - Les obstacles sont des vaisseaux spaciaux

## Contributeurs
- Ashwin KUGARUBAN : *ashwin.kugaruban@efrei.net*
  - Coach/Leader
  - Cartes
- Pablo BIRAN : *pablo.biran@efrei.net*
  - Git/Github
  - Equations de la trajectoire (phase lancée)
- Minh LE : *minh.le@efrei.net*
  - Skins/Tenues
- Thibault DOMMES : *thibault.dommes@efrei.net*
  - Ecran d'accueil
  - Trajectoire (phase descente)
- Mathieu HA : *mathieu.ha@efrei.net*
  - Cartes
  - Ecran d'accueil
