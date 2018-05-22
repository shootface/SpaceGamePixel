import threading
import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from nave import Nave
from Sonda import Sonda
from robot import Robot

class Proceso:
    def __init__(self,idProceso,quantum,nombre,recurso,t,tr):
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
        self.estado=0  #0:listo ; 1:blo ; 2:sus ; 3:ejecucion ; 4:terminado
    
    def __str__(self):
        return self.nombre+" "+str(self.idProceso)
    
    def procesar(self):
        self.quantum-=1
        self.t-=1
        self.zc+=1
        print("Preparando",self.nombre,self.idProceso,"quantum",self.quantum,"t",self.t,"recurso",self.recurso)
    
class ataque(Sprite,Proceso):
    def __init__(self,idProceso,recurso,posX , posY,quantum=0,nombre="ataque planeta",t=18,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)
        Sprite.__init__(self)
        self.disparoNave = Nave()
        self.disparoNave.rect.top = posY
        self.disparoNave.rect.left = posX
        self.disparoNave.disparada = True

class espiar(Sprite,Proceso):
    def __init__(self,idProceso,recurso,posX , posY,quantum=0,nombre="Espiar",t=10,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)
        Sprite.__init__(self)
        self.disparoSonda = Sonda()
        self.disparoSonda.rect.top = posY
        self.disparoSonda.rect.left = posX
        self.disparoSonda.disparada = True

class reciclar(Sprite,Proceso):
    def __init__(self,idProceso,recurso,posX , posY,quantum=0,nombre="reciclar escombros",t=30,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)
        Sprite.__init__(self)
        self.disparoRobot = Robot()
        self.disparoRobot.rect.top = posY
        self.disparoRobot.rect.left = posX
        self.disparoRobot.disparada = True
