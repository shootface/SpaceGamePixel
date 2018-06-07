import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Hangar(Sprite):
    def __init__(self,texto,posXT,posYT,posX,posY,color,nombre="hangar"):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/hangar.jpg").convert()
        self.rect = self.image.get_rect()
        self.texto = texto
        self.fuente1 = pygame.font.Font(None,20)
        self.textoPrioridad = self.fuente1.render(self.texto,1,color)
        self.posXT = posXT
        self.posYT = posYT
        self.posX = posX
        self.posY = posY
    
    def dibujar(self,ventana):
        ventana.blit(self.image,(self.posX,self.posY))
        ventana.blit(self.textoPrioridad,(self.posXT,self.posYT))