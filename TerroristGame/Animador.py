import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Animations import SpaceAtack
import time

class SpaceAtackIntro():
    
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((1000,800))
        self.espacio = espacio()

    def inciar(self):
        self.espacio.cargarImagenes()
        inicio = True
        cont = 0
        while inicio:
            self.espacio.dibujar(self.ventana)
            cont+=1
            if cont == 73:
                inicio = False

class espacio(Sprite):
    def __init__(self,posX=0,posY=0,nombre="espacio"):
        Sprite.__init__(self)
        self.images = list()

    def cargarImagenes(self):
        for i in range(73):
            strH = str(i) + '.gif'
            self.images.append(pygame.image.load("Space/espacioGIF/"+strH))
    
    def dibujar(self,ventana):
        for j in range(73):
            ventana.blit(self.images[j],(0,0))
            pygame.display.update()
            time.sleep(0.1)

cliente = SpaceAtackIntro()
cliente.inciar()