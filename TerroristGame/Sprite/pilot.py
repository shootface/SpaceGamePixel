import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from recursos import Recursos

class pilot(Recursos,Sprite):
    def __init__(self,nombre = "piloto"):
        Sprite.__init__(self)
        Recursos.__init__(self, nombre)
        self.image = pygame.image.load("Space/pilot.png")
        self.imageUse = pygame.image.load("Space/pilotUse.png")

    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(930,200))
    
    def dibujar_Recurso_Uso(self,ventana):
        ventana.blit(self.imageUse,(930,200))
