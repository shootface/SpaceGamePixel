import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Planeta2(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/planeta2.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 100
    
    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)