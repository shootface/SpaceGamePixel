import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from recursos import Recursos

class pilot(Recursos,Sprite):
    def __init__(self,nombre = "Espia"):
        Sprite.__init__(self)
        self.image = pygame.image.load("Space/pilot.png")

    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(930,200))
