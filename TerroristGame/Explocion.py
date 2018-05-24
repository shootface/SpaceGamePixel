import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class explocion(Sprite):
    def __init__(self,posX,posY,nombre="Explocion"):
        Sprite.__init__(self)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left = posX
        self.rect.top = posY
    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)