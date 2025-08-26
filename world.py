import pygame
import constantes

#Las mecanicas de nuestro mundo
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self, screen):
        screen.fill(constantes.GREEN)#vamos a rellenar nuestro mundo de verde
        
