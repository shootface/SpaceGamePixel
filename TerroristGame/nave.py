import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from Explocion import explocion
import time

class Nave(Sprite):
    def __init__(self,nombre="nave"):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/nave.png").convert()
        self.imageSu = pygame.image.load("Space/naveSus.png").convert()
        self.imageBlo = pygame.image.load("Space/naveBlo.png").convert()
        self.imageef = pygame.image.load("Space/explocion.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.velocidad = 100
        self.disparada = False
        self.bloqueada = False
        self.suspendida = False
        self.efecto = True
        
    def trayectoria(self):    
        self.rect.top = self.rect.top - self.velocidad
        print("TOP : ",self.rect.top)
        if self.rect.top < 100:
            self.image = self.imageef
            self.velocidad = 1
            print("EXPLOTANDO")
        if self.rect.top < 19:
            self.disparada = False


    def dibujar(self, ventana):
        ventana.blit(self.image,self.rect)
    def dibujarSu(self,ventana):
        ventana.blit(self.imageSu,self.rect)
    def dibujarBlo(self,ventana):
        ventana.blit(self.imageBlo,self.rect)
    def dibujarEf(self,ventana):
        if self.efecto:  
            print("EFECTO")
            explo = explocion(self.rect.left,100)
            explo.dibujar(ventana)
            self.efecto = False
        else:
            print("YA NO EFECTO")