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

    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidad

    def back(self):
        self.rect.top = 719
        print("BACK-----------------------------------------------------------------------------------")