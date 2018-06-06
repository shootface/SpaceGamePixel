import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from recursos import Recursos

class Sonda(Recursos,Sprite):

    def __init__(self,nombre="Sonda"):
        BLANCO = (255, 255, 255)
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/sonda.png").convert()
        self.imageSu = pygame.image.load("Space/sondaSu.png").convert()
        self.imageBlo = pygame.image.load("Space/sondaBlo.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.velocidad = 150
        self.disparada = False  
        self.bloqueada = False
        self.suspendida = False      

    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)

    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidad
        if self.rect.top < 100:
            self.disparada = False

    def dibujarSu(self,ventana):
        ventana.blit(self.imageSu,self.rect)
    def dibujarBlo(self,ventana):
        ventana.blit(self.imageBlo,self.rect)
