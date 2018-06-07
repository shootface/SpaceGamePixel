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
from Sprite.hangar import Hangar
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
        self.ventana = pygame.display.set_mode((1420,800))

        #Nombre de la ventana
        pygame.display.set_caption("SpaceAtack")
        #Fondo
        self.Space_imageBackground = pygame.image.load("Space/Space.jpg").convert()
        # Definimos algunos colores
        self.BLANCO = (255, 255, 255)
        self.NEGRO = (0, 0, 0)
        self.ROJO = (255,0,0)
        self.VERDE = (0,255,0)
        self.AZUL = (0,0,255)
        #Jugardor principal
        self.jugador = Principal()
        self.planetas = [Planeta1(),Planeta2(),Planeta3()]#Todos los planetas se crean en esta lista
        self.asteroides = [asteroid(220,700),asteroid(630,700)]#Todos los asteroides se crean en esta lista 
        self.recursos = [pilot(),spy(),Mechanic()] #Todos los recursos se crean en una lista
        self.hangares = [Hangar("prioridad MAX",1075,10,1068,0,self.ROJO),Hangar("prioridad MED",1075,277,1068,267,self.VERDE),Hangar("prioridad MIN",1075,543,1068,533,self.AZUL)]
        self.velocidad = 100

        #Colas donde se almacenan los procesos
        self.cola1 = Queue.Queue()
        self.cola2 = Queue.Queue()
        self.cola3 = Queue.Queue()

        #Almacenamiento de los procesos 
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

        #Variables iniciales de posicionamiento
        self.posMin = [(1100,590),(1130,590),(1160,590),(1190,590),(1220,590),(1250,590),(1280,590),(1310,590),(1340,590),(1370,590)]
        self.posMid = [(1100,331),(1130,331),(1160,331),(1190,331),(1220,331),(1250,331),(1280,331),(1310,331),(1340,331),(1370,331)]
        self.posMax = [(1100,60),(1130,60),(1160,60),(1190,60),(1220,60),(1250,60),(1280,60),(1310,60),(1340,60),(1370,60)]
        self.boolposMin = [0,0,0,0,0,0,0,0,0,0]
        self.boolposMid= [0,0,0,0,0,0,0,0,0,0]
        self.boolposMax = [0,0,0,0,0,0,0,0,0,0]

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
            for h in self.hangares:
                h.dibujar(self.ventana)
            
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
                    #self.dibujarPrioridad(x.disparo)
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
            print pygame.mouse.get_pos()
            pygame.display.update()

    def dispararNave(self,posX ,posY,prioridad):
        pos = self.dibujarPrioridad(prioridad)
        #print("POS ENVIADA",pos)
        proceso = ataque(self.numeroAtaque,prioridad,self.recursos[0],posX,self.ventana,posY,pos)
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
        pos = self.dibujarPrioridad(prioridad)
        proceso = espiar(self.numeroAtaque,prioridad,self.recursos[1],posX,self.ventana,posY,pos)
        self.numeroAtaque +=1
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
        pos = self.dibujarPrioridad(prioridad)
        proceso = reciclar(self.numeroAtaque,prioridad,self.recursos[2],posX,self.ventana,posY,pos)
        self.numeroAtaque +=1
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

    def dibujarPrioridad(self,prioridad):
        if prioridad==0:
            print("PRIORIDAD 0")
            for x in range(len(self.posMin)):
                if self.boolposMax[x]==0:
                    self.boolposMax[x]=1
                    return self.posMax[x]
        elif prioridad==1:
            print("PRIORIDAD 1")
            for x in range(len(self.posMin)):
                if self.boolposMid[x]==0:
                    self.boolposMid[x]=1
                    return self.posMid[x]
        elif prioridad==2:
            print("PRIORIDAD 2")
            for x in range(len(self.posMin)):
                if self.boolposMin[x]==0:
                    self.boolposMin[x]=1
                    return self.posMin[x]
            