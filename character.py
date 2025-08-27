import pygame
import constantes

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.inventory = {"wood":0} #lo que puede tener nuestro personaje, ahora tiene 0 madera
        # Donde aparecerá nuestro personaje, en qué coordenadas
        # Tamaño en px del personaje

    def draw(self, screen):
        # Dibujamos nuestro personaje
        pygame.draw.rect(screen, constantes.BLUE, rect=(self.x, self.y, self.size, self.size))

    def move(self, dx, dy):
        # Cómo se mueve el personaje en las coordenadas
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, constantes.WIDTH - self.size)) #para que no se salga de la pantalla
        self.y = max(0, min(self.y, constantes.HEIGHT - self.size)) #para que no se salga de la pantalla
