import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from recursos import Recursos

class Mechanic(Recursos,Sprite):

    def __init__(self,nombre="Mecanico"):
        Sprite.__init__(self)
        Recursos.__init__(self, nombre)
        BLANCO = (255, 255, 255)
        self.image = pygame.image.load("Space/mechanic.png").convert()
        self.image.set_colorkey(BLANCO)
        self.imageUse = pygame.image.load("Space/mechanicUse.png").convert()
    
    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(930,450))

    def dibujar_Recurso_Uso(self,ventana):
        ventana.blit(self.imageUse,(930,450))    

        