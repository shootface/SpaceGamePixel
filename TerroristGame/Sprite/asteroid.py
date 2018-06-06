import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class asteroid(Sprite):
    def __init__(self,posX,posY,nombre="Asteroide"):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/Asteroid.png").convert()
        self.rect = self.image.get_rect()
        self.rect.left = posX
        self.rect.top = posY
    
    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)