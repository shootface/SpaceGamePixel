import pygame 
from pygame.sprite import Sprite
from pygame.locals import *

class Recursos:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libre=True
    
    def __str__(self):
        return(self.nombre)
    
    def utilizar(self):
        if self.libre:
            print("Usando el",self.nombre)
        else:
            print("el",self.nombre,"esta ocupado")
    def liberar(self):
        if not self.libre:
            print("el",self.nombre,"fue liberado")
            self.libre=True
        else:
            print("el",self.nombre,"no estaba siendo usado")

class Nave(Recursos,Sprite):
    def __init__(self,cont_size,nombre="nave"):
        Recursos.__init__(self,nombre)
        sprite.__init__(self)
        self.cont_size = cont_size
        self.image = pygame.image.load("Space/nave.png").convert()
        self.rect = self.image.get_rect()
        self.rect.move_ip(cont_size[0]-100,cont_size[1]-700)     
class Sonda(Recursos,Sprite):
    def __init__(self,cont_size,nombre="Sonda"):
        Recursos.__init__(self,nombre)
        sprite.__init__(self)
        self.cont_size = cont_size
        self.image = pygame.image.load("Space/sonda.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(cont_size[0]-100,cont_size[1]-550)
class Robots(Recursos,Sprite):
    def __init__(self,cont_size,nombre="Robots"):
        Recursos.__init__(self,nombre)
        sprite.__init__(self)
        self.cont_size = cont_size
        self.image = pygame.image.load("Space/robots.png").convert()
        self.rect = self.image.get_rect()
        self.rect.move_ip(cont_size[0]-100,cont_size[1]-400)