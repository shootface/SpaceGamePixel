import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from Explocion import explocion
import time

class Nave(Sprite):
    def __init__(self,posMini,prioridad,id,nombre="nave"):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/nave.png").convert()
        self.imageSu = pygame.image.load("Space/naveSus.png").convert()
        self.imageBlo = pygame.image.load("Space/naveBlo.png").convert()
        self.imageef = pygame.image.load("Space/explocion.png").convert()
        self.imageMini = pygame.image.load("Space/naveMini.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.velocidad = 100
        self.disparada = False
        self.bloqueada = False
        self.suspendida = False
        self.efecto = True
        self.priodidad = prioridad
        self.id = id
        self.fuente1 = pygame.font.Font(None,25)
        self.textoID = self.fuente1.render(str(self.id),1,(204, 51, 255))
        self.pos=posMini
        print("POS MINI",posMini)
        
    def trayectoria(self):    
        self.rect.top = self.rect.top - self.velocidad
        if self.rect.top < 100:
            self.disparada = False
        
    def getPrioridad(self):
        return self.priodidad

    def dibujar(self, ventana):
        ventana.blit(self.image,self.rect)
        ventana.blit(self.textoID,(self.rect.left-20,self.rect.top))
        self.dibujarMiniatura(ventana)

    def dibujarSu(self,ventana):
        ventana.blit(self.imageSu,self.rect)
        ventana.blit(self.textoID,(self.rect.left-20,self.rect.top))

    def dibujarBlo(self,ventana):
        ventana.blit(self.imageBlo,self.rect)
        ventana.blit(self.textoID,(self.rect.left-20,self.rect.top))

    def dibujarMiniatura(self,ventana):
        ventana.blit(self.imageMini,self.pos)
        ventana.blit(self.textoID,(self.pos[0]-5,self.pos[1]))