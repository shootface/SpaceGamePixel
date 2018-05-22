import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Nave(Sprite):
    def __init__(self,nombre="nave"):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/nave.png").convert()
        self.imageFreez = pygame.image.load("Space/navefrezz.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.velocidad = 100
        self.disparada = False
        
    def trayectoria(self):    
        self.rect.top = self.rect.top - self.velocidad
        #print("TOP : ",self.rect.top)
        if self.rect.top < 100:
            self.disparada = False

    def dibujar(self, ventana):
        ventana.blit(self.image,self.rect)

    def dibujarFreez(self,ventana):
        ventana.blit(self.imageFreez,self.rect)