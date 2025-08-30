import pygame
import constantes
import os 
class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.inventory = {"wood":0} #lo que puede tener nuestro personaje, ahora tiene 0 madera
        # Donde aparecerá nuestro personaje, en qué coordenadas
        # Tamaño en px del personaje
        image_path = os.path.join("assets", "images", "character", "personaje.png")
        self.image = pygame.image.load(image_path).convert_alpha() #para guardar la imagen como parametro
        self.image = pygame.transform.scale(self.image, (constantes.PERSONAJE, constantes.PERSONAJE)) #para redimensionar la imagen
        self.size = self.image.get_width() 
        
        
    def draw(self, screen):
        # Dibujamos nuestro personaje
        screen.blit(self.image, (self.x, self.y))
        
        
    def move(self, dx, dy):
        # Cómo se mueve el personaje en las coordenadas
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, constantes.WIDTH - self.size)) #para que no se salga de la pantalla
        self.y = max(0, min(self.y, constantes.HEIGHT - self.size)) #para que no se salga de la pantalla
