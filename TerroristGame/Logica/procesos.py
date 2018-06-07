import threading
import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from Sprite.nave import Nave
from Sprite.Sonda import Sonda
from Sprite.robot import Robot

class Proceso:
    def __init__(self,idProceso,prioridad,quantum,nombre,recurso,t,tr,ventana):
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
        self.te=0
        self.prioridad=prioridad #0:max ; 1:med ; 2:min
        self.estado=0  #0:listo ; 1:bloqueado ; 2:suspendido ; 3:ejecucion ; 4:terminado
        self.ventana = ventana
    
    def __str__(self):
        return self.nombre+" "+str(self.idProceso)
    
    def procesar(self):
        self.estado=3
        if self.prioridad==0:
            self.quantum-=1
        self.t-=1
        self.zc+=1
        if self.estado == 3:
            self.disparo.trayectoria()
            self.disparo.bloqueada = False
            self.disparo.suspendida = False
        print("Preparando",self.nombre,self.idProceso,"quantum",self.quantum,"t",self.t,"recurso",self.recurso)

    def bloqueado(self):
        print("Bloqueado")
        self.estado = 1
        self.disparo.bloqueada = True

    def suspendido(self):
        print("Suspendido")
        self.disparo.suspendida = True
        self.tr=5
        self.estado=2
        self.recurso.liberar()
    
    def asignarTiempoEnvejecimiento(self,ttotal):
        cons=20
        if self.t>=ttotal*0.7:
            self.te=cons
        elif self.t>=ttotal*0.4:
            self.te=cons*1.5
        else:
            self.te=cons*2.5

class ataque(Sprite,Proceso):
    
    def __init__(self,idProceso,prioridad,recurso,posX ,ventana, posY,pos,quantum=0,nombre="ataque planeta",t=8,tr=0,):
        Proceso.__init__(self,idProceso,prioridad,quantum,nombre,recurso,t,tr,ventana)
        Sprite.__init__(self)
        self.disparo = Nave(pos,prioridad,idProceso)
        self.disparo.rect.top = posY
        self.disparo.rect.left = posX
        self.disparo.disparada = True

class espiar(Sprite,Proceso):
    
    def __init__(self,idProceso,prioridad,recurso,posX ,ventana, posY,quantum=0,nombre="Espiar",t=5,tr=0):
        Proceso.__init__(self,idProceso,prioridad,quantum,nombre,recurso,t,tr,ventana)
        Sprite.__init__(self)
        self.disparo = Sonda(prioridad,idProceso)
        self.disparo.rect.top = posY
        self.disparo.rect.left = posX
        self.disparo.disparada = True

class reciclar(Sprite,Proceso):
    
    def __init__(self,idProceso,prioridad,recurso,posX ,ventana, posY,quantum=0,nombre="reciclar escombros",t=12,tr=0):
        Proceso.__init__(self,idProceso,prioridad,quantum,nombre,recurso,t,tr,ventana)
        Sprite.__init__(self)
        self.disparo = Robot(prioridad,idProceso)
        self.disparo.rect.top = posY
        self.disparo.rect.left = posX
        self.disparo.disparada = True
