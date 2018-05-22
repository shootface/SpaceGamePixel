import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Nave(Sprite):
    def __init__(self,nombre="nave"):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/nave.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.velocidad = 10
        self.disparada = False
        
    def trayectoria(self):    
        self.rect.top = self.rect.top - self.velocidad
        #print("TOP : ",self.rect.top)
        if self.rect.top < 100:
            self.disparada = False
    
    def back(self):
        self.rect.top = 719
        print("BACK-----------------------------------------------------------------------------------")

    def dibujar(self, ventana):
        ventana.blit(self.image,self.rect)

    def bloqueado(self):
        self.rect.top = 65
        self.rect.left = 80