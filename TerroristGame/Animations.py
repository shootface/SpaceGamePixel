import pygame,sys
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

def SpaceAtack():
    pygame.init()
    #Tamano de la ventana
    ventana = pygame.display.set_mode((1000,800))
    #Nombre de la ventana
    pygame.display.set_caption("SpaceAtack")
    #Fondo
    Space_imageBackground = pygame.image.load("Space/Space.jpg").convert()
    # Definimos algunos colores
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    #Jugardor principal
    jugador = Principal()
    planeta1 = Planeta1()
    planeta2 = Planeta2()
    planeta3 = Planeta3()
    naveRecurso = Nave()
    sondaRecurso = Sonda()
    robotRecurso = Robot()
    disparoNave = Nave()
    velocidad = 8
    def animarNave(jugador):
        disparoNave.dibujar(ventana)
        return
    #Hilos de ejecucion 
    t1 = threading.Thread(name="hilo_1", target=animarNave, args=(jugador, ))
    #Ejecucion animaciones
    while True:
        ventana.blit(Space_imageBackground,(0,0))
        jugador.dibujar(ventana)
        planeta1.dibujar(ventana)
        planeta2.dibujar(ventana)
        planeta3.dibujar(ventana)
        naveRecurso.dibujar_Recurso(ventana)
        sondaRecurso.dibujar_Recurso(ventana)
        robotRecurso.dibujar_Recurso(ventana)
        disparoNave.trayectoria()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    jugador.mover(jugador.get_posX()-velocidad)
                elif event.key == K_RIGHT:
                    jugador.mover(jugador.get_posX()+velocidad)
                elif event.key == K_z:
                    
        print pygame.mouse.get_pos()
        pygame.display.update()

SpaceAtack()