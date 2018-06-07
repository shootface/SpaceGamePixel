import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from Logica.recursos import Recursos

class Robot(Recursos,Sprite):

    def __init__(self,posMini,prioridad,id,nombre="Robot"):
        Sprite.__init__(self)
        BLANCO = (255, 255, 255)
        self.image = pygame.image.load("Space/robot.png").convert()
        self.imageSu = pygame.image.load("Space/robotSu.png").convert()
        self.imageSu.set_colorkey((0,0,0))
        self.imageBlo = pygame.image.load("Space/robotBlo.png").convert()
        self.imageMini = pygame.image.load("Space/robotMini.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.id = id
        self.fuente1 = pygame.font.Font(None,25)
        self.textoID = self.fuente1.render(str(self.id),1,(204, 51, 255))
        self.velocidad = 59
        self.disparada = False
        self.bloqueada = False
        self.suspendida = False 
        self.pos=posMini  

    def dibujar(self,ventana):
        ventana.blit(self.image,self.rect)
        ventana.blit(self.textoID,(self.rect.left-20,self.rect.top))
        self.dibujarMiniatura(ventana)

    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidad
        if self.rect.top < 100:
            self.disparada = False

    def dibujarSu(self,ventana):
        ventana.blit(self.imageSu,self.rect)

    def dibujarBlo(self,ventana):
        ventana.blit(self.imageBlo,self.rect)

    def dibujarMiniatura(self,ventana):
        ventana.blit(self.imageMini,self.pos)
        ventana.blit(self.textoID,(self.pos[0]-5,self.pos[1]))