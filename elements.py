import pygame
import constantes

class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 40
        self.wood = 5 #va a entregar 5 de madera
        
        
    def draw(self, screen):
        pygame.draw.rect(screen, constantes.BROWN, rect=(self.x, self.y, self.size, self.size))