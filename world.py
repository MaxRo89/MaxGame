import pygame
import constantes
from elements import Tree
import random


#Las mecanicas de nuestro mundo
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.trees = [Tree(random.randint(0, width-40), 
                           random.randint(0, height-40)) for _ in range(10)] #vamos a crear 10 arboles de forma aleatoria
        
        
    def draw(self, screen):
        screen.fill(constantes.GREEN)#vamos a rellenar nuestro mundo de verde
        for tree in self.trees:
            tree.draw(screen)
