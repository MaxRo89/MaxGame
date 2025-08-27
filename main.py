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
    
        keys = pygame.key.get_pressed() #guardara la tecla del teclado
        if keys[pygame.K_LEFT]:
            character.move(-5, dy=0)
        if keys[pygame.K_RIGHT]:        
            character.move(dx=5, dy=0)
        if keys[pygame.K_UP]:        
            character.move(dx=0, dy=-5)
        if keys[pygame.K_DOWN]:        
            character.move(dx=0, dy=5)

        
        world.draw(ventana)
        character.draw(ventana)
        pygame.display.flip() #activamos la visualizacion de la ventana
        clock.tick(60) #los fps de nuestro juego


if __name__ == "__main__":
    main()
            