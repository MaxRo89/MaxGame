import pygame
import constantes
from elements import Tree
import random
import os

#Las mecanicas de nuestro mundo
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.trees = [Tree(random.randint(0, width-40), 
                           random.randint(0, height-40)) for _ in range(10)] #vamos a crear 10 arboles de forma aleatoria
        
        image_path = os.path.join("assets", "images", "objects", "pasto.png")
        self.grass_image = pygame.image.load(image_path).convert() #para guardar la imagen como parametro
        self.grass_image = pygame.transform.scale(self.grass_image, (constantes.PASTO, constantes.PASTO)) #para redimensionar la imagen

        
    def draw(self, screen):
        for y in range(0, self.height, constantes.PASTO):
            for x in range(0, self.width, constantes.PASTO):
                screen.blit(self.grass_image, (x, y))
                # dibujamos el pasto en todo el mundo
                
        for tree in self.trees:
            tree.draw(screen)
