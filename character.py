import pygame
import constantes

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
#Donde aparacera nuestro personaje, en que cordenadas
#Tamano de px del personaje
    def draw(self, screen):
     pygame.draw.rect(screen, constantes.BLUE,  rect= (self.x, self.y, self.size, self.size))
     #dibujamos nuestro personaje
     
     def move(self, dx, dy): #como se mueve el personaje en las coordenadas
         self.x += dx
         self.x += dy
         