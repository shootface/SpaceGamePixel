import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Sonda(Sprite):

    def __init__(self):
        BLANCO = (255, 255, 255)
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/sonda.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()

    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)

    def set_rect(self,posX,posY):
        self.rect.x = posX
        self.rect.y = posY
    
    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(850,330))