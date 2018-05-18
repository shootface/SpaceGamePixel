import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Principal(Sprite):
    def __init__(self,cont_size):
        Sprite.__init__(self)
        self.cont_size = cont_size
        self.image =pygame.image.load("Space/planeta1.jpg").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.centery = 720
        
    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)