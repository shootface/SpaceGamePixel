import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Animations import SpaceAtack
import time

class espacio(Sprite):
    def __init__(self,posX=0,posY=0,nombre="espacio"):
        Sprite.__init__(self)
        self.images = list()
        
        self.rect.left = posX
        self.rect.top = posY

    def cargarImagenes(self):
        for i in range(73):
            str = i + '.gif'
            self.images.append(pygame.image.load("Space/espacioGIF/"+str))
    
    def dibujar(self,ventana):
        for j in range(73):
            ventana.blit(self.images[j],(0,0)

class ventanaInicio():
    def __init__(self):
        self.ventanaInicio = pygame.display.set_mode((1000,800))
        self.espacio = espacio()

    def inciar(self):
        self.espacio.cargarImagenes()
        inicio = True
        cont = 0
        while inicio:
            self.espacio.dibujar(self.ventanaInicio)
            pygame.display.update()
            cont+=1
            if cont == 73:
                inicio = False

        juego = SpaceAttack()
        juego.iniciar()


inicio = ventanaInicio()
inicio.inciar()
        