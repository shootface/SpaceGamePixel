import threading
import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from nave import Nave
from Sonda import Sonda
from robot import Robot

class Proceso:
    def __init__(self,idProceso,quantum,nombre,recurso,t,tr,ventana):
        self.idProceso = idProceso
        self.nombre=nombre
        self.recurso=recurso
        self.t=t
        self.tr=tr
        self.quantum=quantum
        self.sus=0
        self.blo=0
        self.lis=0
        self.zc=0
        self.estado=0  #0:listo ; 1:bloqueado ; 2:suspendido ; 3:ejecucion ; 4:terminado
        self.ventana = ventana
    
    def __str__(self):
        return self.nombre+" "+str(self.idProceso)
    
    def procesar(self):
        self.quantum-=1
        self.t-=1
        self.zc+=1
        if self.estado == 3:
            print("HOLA")
            self.disparo.dibujar(self.ventana)
            self.disparo.trayectoria()
            pygame.display.update()
        if self.estado == 1:
            self.disparo.bloqueado()
            self.disparo.dibujar(self.ventana)
        if self.estado == 2:
            self.disparo.dibujar(self.ventana)
        print("Preparando",self.nombre,self.idProceso,"quantum",self.quantum,"t",self.t,"recurso",self.recurso)

class ataque(Sprite,Proceso):
    
    def __init__(self,idProceso,recurso,posX ,ventana, posY,quantum=0,nombre="ataque planeta",t=8,tr=0,):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr,ventana)
        Sprite.__init__(self)
        self.disparo = Nave()
        self.disparo.rect.top = posY
        self.disparo.rect.left = posX
        self.disparo.disparada = True

class espiar(Sprite,Proceso):
    
    def __init__(self,idProceso,recurso,posX , posY,quantum=0,nombre="Espiar",t=5,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)
        Sprite.__init__(self)
        self.disparo = Sonda()
        self.disparo.rect.top = posY
        self.disparo.rect.left = posX
        self.disparo.disparada = True
    
    def espiarBloqueado(self):
        self.disparo.rect.top = 260
        self.disparo.rect.top = 80
    
    def espiasSuspendido(self):
        self.disparoSonda.rect.top = self.disparoSonda.rect.top

class reciclar(Sprite,Proceso):
    
    def __init__(self,idProceso,recurso,posX , posY,quantum=0,nombre="reciclar escombros",t=12,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)
        Sprite.__init__(self)
        self.disparoRobot = Robot()
        self.disparoRobot.rect.top = posY
        self.disparoRobot.rect.left = posX
        self.disparoRobot.disparada = True
    
    def reciclarBloqueado(self):
        self.disparoRobot.rect.top = 630
        self.disparoRobot.rect.top = 80
    
    def reciclarSuspendido(self):
        self.disparoRobot.rect.top = self.disparoRobot.rect.top

