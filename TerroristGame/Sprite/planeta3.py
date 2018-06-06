import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Planeta3(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        BLANCO = (255, 255, 255)
        self.image = pygame.image.load("Space/planeta3.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = 800
        self.rect.centery = 100
    
    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)