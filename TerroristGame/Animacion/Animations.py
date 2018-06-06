import pygame
import sys
import threading
import Queue
import time
from Logica.trayecto import Trayecto
from pygame.locals import *
from Logica.recursos import *
from Sprite.principal import Principal
from Sprite.Planeta1 import Planeta1
from Sprite.planeta2 import Planeta2
from Sprite.planeta3 import Planeta3
from Sprite.asteroid import asteroid
from Sprite.Explocion import explocion
from Sprite.mechanic import Mechanic
from Sprite.spy import spy
from Sprite.pilot import pilot
from Logica.procesos import *
import time

listaNave = []
listaSondas = []
listaRobots = []

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
        self.planetas = [Planeta1(),Planeta2(),Planeta3()]#Todos los planetas se crean en esta lista
        self.asteroides = [asteroid(220,700),asteroid(630,700)]#Todos los asteroides se crean en esta lista 
        self.recursos = [pilot(),spy(),Mechanic()] #Todos los recursos se crean en una lista
        self.velocidad = 100

        #Colas donde se almacenan los procesos
        self.cola1 = Queue.Queue()
        self.cola2 = Queue.Queue()
        self.cola3 = Queue.Queue()

        self.lisProcesos1 = list()
        self.lisProcesos2 = list()
        self.lisProcesos3 = list()

        #Definicion de procesadores
        self.procesador1 = Trayecto(1, self.cola1)
        self.procesador2 = Trayecto(2, self.cola2)
        self.procesador3 = Trayecto(3, self.cola3)

        #Variables de conteo para el  id del proceso 
        self.numeroAtaque = 0
        self.numeroEspiar = 0
        self.numeroReciclar = 0

        #objeto quantum
    def iniciar(self):            

        self.hiloAnimacionEntradas = threading.Thread(name="animacion entradas", target = self.animacionEntradas)
        self.hiloAnimacionEntradas.setDaemon(True)

        self.hilos = [self.procesador1, self.procesador2, self.procesador3, self.hiloAnimacionEntradas]
        for hilo in self.hilos:
            hilo.start()

        self.cola1.join()
        self.cola2.join()
        self.cola3.join()
        self.hiloAnimacionEntradas.join()

    def animacionEntradas(self):
        while True:
            self.ventana.blit(self.Space_imageBackground,(0,0))
            for r in self.recursos:
                if r.libre:
                    r.dibujar_Recurso(self.ventana) #Se recorre la lista para dibuajr los recursos en el lateral de la ventana
                else:
                    print(r.nombre,"ESTA OCUPADO")
                    r.dibujar_Recurso_Uso(self.ventana)
            for p in self.planetas:
                p.dibujar(self.ventana)
            for a in self.asteroides:
                a.dibujar(self.ventana)
            
            self.jugador.dibujar(self.ventana)

            for event in pygame.event.get():
                if event.type == K_p:
                    pygame.quit()
                    for hilo in self.hilos:
                        hilo.exit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    mod_bitmask = pygame.key.get_mods()
                    if mod_bitmask & pygame.KMOD_CTRL:
                        prioridad=2
                    elif mod_bitmask & pygame.KMOD_SHIFT:
                        prioridad=0
                    else:
                        prioridad=1
                    if event.key == K_p:
                        pygame.quit()
                        for hilo in self.hilos:
                            hilo.exit()
                        sys.exit()
                    if event.key == K_LEFT:
                        self.jugador.mover(self.jugador.get_posX()-self.velocidad)
                    elif event.key == K_RIGHT:
                        self.jugador.mover(self.jugador.get_posX()+self.velocidad)
                    elif event.key == K_z:
                        x,y = self.jugador.rect.center
                        self.dispararNave(x,y,prioridad)
                    elif event.key == K_x:
                        x,y = self.jugador.rect.center
                        self.dispararSonda(x,y,prioridad)
                    elif event.key == K_c:
                        x,y = self.jugador.rect.center
                        self.dispararRobots(x,y,prioridad)
            if len(listaNave)>0:
                #print("Tanano lista :",len(listaNave))
                for x in listaNave:
                    if x.disparo.disparada:
                        x.disparo.dibujar(self.ventana)
                    if x.disparo.bloqueada:
                        x.disparo.dibujarBlo(self.ventana)
                    if x.disparo.suspendida:
                        x.disparo.dibujarSu(self.ventana)
            if len(listaSondas)>0:
                for x in listaSondas:
                    if x.disparo.disparada:
                        x.disparo.dibujar(self.ventana)
                    if x.disparo.bloqueada:
                        x.disparo.dibujarBlo(self.ventana)
                    if x.disparo.suspendida:
                        x.disparo.dibujarSu(self.ventana)
            if len(listaRobots)>0:
                for x in listaRobots:
                    if x.disparo.disparada:
                        x.disparo.dibujar(self.ventana)
                    if x.disparo.bloqueada:
                        x.disparo.dibujarBlo(self.ventana)
                    if x.disparo.suspendida:
                        x.disparo.dibujarSu(self.ventana)
            #print pygame.mouse.get_pos()
            pygame.display.update()

    def dispararNave(self,posX ,posY,prioridad):
        proceso = ataque(self.numeroAtaque,prioridad,self.recursos[0],posX,self.ventana,posY)
        self.numeroAtaque +=1
        if posX<=220:
            self.cola1.put(proceso)
            estado = "Atacando el planeta 1"
            self.procesador1.estado = estado
        elif posX>220 and posX <= 630:
            self.cola2.put(proceso)
            estado = "Atacando el planeta 2"
            self.procesador2.estado = estado
        elif posX > 630:
            self.cola3.put(proceso)
            estado = "Atacando el planeta 3"
            self.procesador3.estado = estado
        listaNave.append(proceso)

    def  dispararSonda(self,posX, posY,prioridad):
        proceso = espiar(self.numeroEspiar,prioridad,self.recursos[1],posX,self.ventana,posY)
        self.numeroEspiar +=1
        if posX<=220:
            self.cola1.put(proceso)
            estado = "Espiando el planeta 1"
            self.procesador1.estado = estado
        elif posX>220 and posX <= 630:
            self.cola2.put(proceso)
            estado = "Espiando el planeta 2"
            self.procesador2.estado = estado
        elif posX > 630:
            self.cola3.put(proceso)
            estado = "Espiando el planeta 3"
            self.procesador3.estado = estado
        listaSondas.append(proceso)

    def dispararRobots(self,posX,posY,prioridad):
        proceso = reciclar(self.numeroReciclar,prioridad,self.recursos[2],posX,self.ventana,posY)
        if posX<=220:
            self.cola1.put(proceso)
            estado = "Reciclar el planeta 1"
            self.procesador1.estado = estado
        elif posX>220 and posX <= 630:
            self.cola2.put(proceso)
            estado = "Reciclar el planeta 2"
            self.procesador2.estado = estado
        elif posX > 630:
            self.cola3.put(proceso)
            estado = "Reciclar el planeta 3"
            self.procesador3.estado = estado
        listaRobots.append(proceso)