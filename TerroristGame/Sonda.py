import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from recursos import Recursos

class Sonda(Recursos,Sprite):

    def __init__(self,nombre="Sonda"):
        BLANCO = (255, 255, 255)
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/sonda.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.velocidad = 1
        self.disparada = False        
    
    def disparar(self, posX , posY):
        self.rect.top = posY
        self.rect.left = posX
        self.disparada = True

    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)

    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidad
    
    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(850,330))