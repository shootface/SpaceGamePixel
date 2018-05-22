import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Mechanic(Sprite):

    def __init__(self,nombre="Mecanico"):
        Sprite.__init__(self)
        BLANCO = (255, 255, 255)
        self.image = pygame.image.load("Space/mechanic.jpg").convert()
        self.image.set_colorkey(BLANCO)
    
    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(930,450))