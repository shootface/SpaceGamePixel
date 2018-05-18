import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Principal(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/principal.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx=500
        self.rect.centery=720
        print("posicion",self.rect.x)

    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)
    
    def mover(self,posX):
        self.rect.x = posX
    
    def get_posX(self):
        return self.rect.x
    
    def get_posY(self):
        return self.rect.y