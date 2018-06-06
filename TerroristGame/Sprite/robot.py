import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from Logica.recursos import Recursos

class Robot(Recursos,Sprite):

    def __init__(self,nombre="Robot"):
        Sprite.__init__(self)
        BLANCO = (255, 255, 255)
        self.image = pygame.image.load("Space/robot.png").convert()
        self.imageSu = pygame.image.load("Space/robotSu.png").convert()
        self.imageSu.set_colorkey((0,0,0))
        self.imageBlo = pygame.image.load("Space/robotBlo.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.velocidad = 59
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