class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        # Initialisation des différentes propriétés du bouton
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input

        # Création du texte à afficher, en utilisant la couleur de base
        self.text = self.font.render(self.text_input, True, self.base_color)

        # Si aucune image n’est fournie, on utilise le texte comme "image" de base
        if self.image is None:
            self.image = self.text

        # Définition des rectangles pour l'image et le texte
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        # Affichage de l’image du bouton
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        # Vérifie si une position donnée est à l’intérieur du bouton
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        # Si la souris est sur le bouton, on change la couleur du texte pour indiquer un survol
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            # Sinon on remet la couleur de base
            self.text = self.font.render(self.text_input, True, self.base_color)
