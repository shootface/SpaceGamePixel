import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from recursos import Recursos

class Nave(Recursos,Sprite):
    def __init__(self,nombre="nave"):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/nave.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.velocidad = 1
        self.disparada = False

    def disparar(self, posX , posY):
        self.rect.top = posY
        self.rect.left = posX
        self.disparada = True

    
    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(900,200))
    
    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidad

    def dibujar(self, ventana):
        ventana.blit(self.image,self.rect)