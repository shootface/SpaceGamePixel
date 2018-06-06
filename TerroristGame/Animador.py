import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Animations import SpaceAtack
import time

class SpaceAtackIntro():
    
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((498,498))
        self.espacio = espacio()

    def inciar(self):
        self.espacio.cargarImagenes()
        self.espacio.dibujar(self.ventana)

        juego = SpaceAtack()
        juego.iniciar()

class espacio(Sprite):
    def __init__(self,posX=0,posY=0,nombre="espacio"):
        Sprite.__init__(self)
        self.images = list()
        self.fuente1 = pygame.font.Font(None,70)
        self.textoBienvenida = self.fuente1.render("SpaceAttack", 1, (255,255,255))

    def cargarImagenes(self):
        for i in range(73):
            strH = str(i) + '.gif'
            self.images.append(pygame.image.load("Space/espacioGIF/"+strH))
    
    def dibujar(self,ventana):
        for j in range(73):
            ventana.blit(self.images[j],(0,0))
            ventana.blit(self.textoBienvenida,(100,249))
            pygame.display.update()
            time.sleep(0.1)

cliente = SpaceAtackIntro()
cliente.inciar()