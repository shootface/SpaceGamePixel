import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from recursos import Recursos

class Robot(Recursos,Sprite):

    def __init__(self,nombre="Robot"):
        Sprite.__init__(self)
        BLANCO = (255, 255, 255)
        self.image = pygame.image.load("Space/robot.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.velocidad = 1
        self.disparada = False   

    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)

    def disparar(self, posX , posY):
        self.rect.top = posY
        self.rect.left = posX
        self.disparada = True
    

    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidad
    
    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(900,450))