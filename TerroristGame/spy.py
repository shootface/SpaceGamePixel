import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from recursos import Recursos

class spy(Recursos,Sprite):

    def __init__(self,nombre = "Espia"):
        Sprite.__init__(self)
        Recursos.__init__(self, nombre)
        BLANCO = (255, 255, 255)
        self.image = pygame.image.load("Space/spy.png")
        self.imageUse = pygame.image.load("Space/spyUse.png")
        self.image.set_colorkey(BLANCO)
    
    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(960,330))
    def dibujar_Recurso_Uso(self,ventana):
        ventana.blit(self.imageUse,(960,330)) 