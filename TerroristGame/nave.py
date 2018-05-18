import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Nave(Sprite):
    
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/nave.png").convert()
        self.rect = self.image.get_rect()
        self.velocidad = 9

    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)

    def set_rect(self,posX,posY):
        self.rect.x = posX
        self.rect.y = posY
    
    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(900,200))
    
    def trayectoria(self):
        self.rect.y = self.rect.y - self.velocidad
        
        
    