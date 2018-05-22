import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class spy(Sprite):

    def __init__(self,nombre = "Espia"):
        BLANCO = (255, 255, 255)
        self.image = pygame.image.load("Space/spy.png")
        self.image.set_colorkey(BLANCO)
    
    def dibujar_Recurso(self,ventana):
        ventana.blit(self.image,(960,330))