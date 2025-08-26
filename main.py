import pygame
import sys
import constantes
from character import Character
from world import World

#iniciliazamos pygame
pygame.init()


WIDTH, HEIGHT = 800,600 #La medida de nuestro juego
ventana = pygame.display.set_mode((constantes.WIDTH, constantes.HEIGHT))
pygame.display.set_caption("Simulador de vida salvaje") #Nombre de la ventana del juego

def main():
    clock = pygame.time.Clock() #para que se vaya actualizando el juego
    world = World(constantes.WIDTH, constantes.HEIGHT)
    character = Character(constantes.WIDTH // 2, constantes.HEIGHT//2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #si apretamos la x de nuestra ventana se sale
                pygame.quit()
                sys.exit()
                
if __name__ == "__main__":
    main()
            