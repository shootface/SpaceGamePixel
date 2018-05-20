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
        self.planeta1 = Planeta1()
        self.planeta2 = Planeta2()
        self.planeta3 = Planeta3()
        self.naveRecurso = Nave()
        self.sondaRecurso = Sonda()
        self.robotRecurso = Robot()
        self.velocidad = 8
        self.disparoNave = Nave()
        #self.disparoNave.set_rect(jugador.get_posX(),jugador.get_posY())
        #self.t1 = threading.Thread(name="hilo_1", target=animrNave, args=(jugador ))
    
    def iniciar(self):
        self.disparoNave.dibujar(self.ventana)
        #Hilos de ejecucion 
        
        print "que heso"
        self.hiloAnimaciones()
        print "que hace"
    
    def hiloAnimaciones(self):
        print "hola"
        while True:
            self.ventana.blit(self.Space_imageBackground,(0,0))
            self.jugador.dibujar(self.ventana)
            self.planeta1.dibujar(self.ventana)
            self.planeta2.dibujar(self.ventana)
            self.planeta3.dibujar(self.ventana)
            self.naveRecurso.dibujar_Recurso(self.ventana)
            self.sondaRecurso.dibujar_Recurso(self.ventana)
            self.robotRecurso.dibujar_Recurso(self.ventana)
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
                        self.t1.start()
            print pygame.mouse.get_pos()
            pygame.display.update()

cliente = SpaceAtack()
cliente.iniciar()