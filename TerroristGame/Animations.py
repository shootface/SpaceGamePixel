import pygame
import sys
from pygame.locals import *
from recursos import *
import threading
from principal import Principal
from Planeta1 import Planeta1
from planeta2 import Planeta2
from planeta3 import Planeta3
from nave import Nave
from Sonda import Sonda
from robot import Robot

listaDisparos = []
listaSondas = []
listaRobots = []

def dispararNave(posX , posY):
    disparoNave = Nave()
    disparoNave.rect.top = posY
    disparoNave.rect.left = posX
    disparoNave.disparada = True
    listaDisparos.append(disparoNave)

def  dispararSonda(posX, posY):
    disparoSonda = Sonda()
    disparoSonda.rect.top = posY
    disparoSonda.rect.left = posX
    disparoSonda.disparada = True
    listaSondas.append(disparoSonda)

def dispararRobots(posX,posY):
    disparoRobot = Robot()
    disparoRobot.rect.top = posY
    disparoRobot.rect.left = posX
    disparoRobot.disparada = True
    listaRobots.append(disparoRobot)

class SpaceAtack():
    def __init__(self):
        pygame.init()
        #Tamano de la ventana
        self.ventana = pygame.display.set_mode((1000,800))
        #Nombre de la ventana
        pygame.display.set_caption("SpaceAtack")
        #Fondo
        self.Space_imageBackground = pygame.image.load("Space/Space.jpg").convert()
        # Definimos algunos colores
        self.BLANCO = (255, 255, 255)
        self.NEGRO = (0, 0, 0)
        #Jugardor principal
        self.jugador = Principal()
        self.planetas = [Planeta1(),Planeta2(),Planeta3()]
        self.recursos = [Nave(),Sonda(),Robot()] #Todos los recursos se crean en una lista
        self.velocidad = 8
    #Ejecucion animaciones

    def iniciar(self):
        self.animacionEntradas();

    def animacionEntradas(self):
        while True:
            self.ventana.blit(self.Space_imageBackground,(0,0))
            self.jugador.dibujar(self.ventana)
            for r in self.recursos:
                r.dibujar_Recurso(self.ventana) #Se recorre la lista para dibuajr los recursos en el lateral de la ventana
            for p in self.planetas:
                p.dibujar(self.ventana)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        self.jugador.mover(self.jugador.get_posX()-self.velocidad)
                    elif event.key == K_RIGHT:
                        self.jugador.mover(self.jugador.get_posX()+self.velocidad)
                    elif event.key == K_z:
                        x,y = self.jugador.rect.center
                        dispararNave(x,y)
                    elif event.key == K_x:
                        x,y = self.jugador.rect.center
                        dispararSonda(x,y)
                    elif event.key == K_c:
                        x,y = self.jugador.rect.center
                        dispararRobots(x,y)
            if len(listaDisparos)>0:
                for x in listaDisparos:
                    if x.disparada:
                        x.dibujar(self.ventana)
                        x.trayectoria()
                    if x.rect.top < 100:
                        x.disparada = False
            if len(listaSondas)>0:
                for x in listaSondas:
                    if x.disparada:
                        x.dibujar(self.ventana)
                        x.trayectoria()
                    if x.rect.top < 100:
                        x.disparada = False
            if len(listaRobots)>0:
                for x in listaRobots:
                    if x.disparada:
                        x.dibujar(self.ventana)
                        x.trayectoria()
                    if x.rect.top < 100:
                        x.disparada = False
            print pygame.mouse.get_pos()
            pygame.display.update()

cliente = SpaceAtack()
cliente.iniciar()