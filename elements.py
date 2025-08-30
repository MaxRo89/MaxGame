import pygame
import constantes
import os


class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wood = 5 #va a entregar 5 de madera
        
        three_path = os.path.join("assets", "images", "objects", "arbol.png")
        self.image = pygame.image.load(three_path).convert_alpha() #para guardar la imagen como parametro
        self.image = pygame.transform.scale(self.image, (constantes.ARBOL, constantes.ARBOL)) #para redimensionar la imagen
        self.size = self.image.get_width()
        
    def draw(self, screen):
        # Dibujamos nuestro arbol
        screen.blit(self.image, (self.x, self.y))
