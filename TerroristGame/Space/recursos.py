import pygame 
from pygame.sprite import sprite
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

class Hangar(Recursos,sprite):
    def __init__(self,cont_size,nombre="Hangar"):
        Recursos.__init__(self,nombre)
        sprite.__init__(self)
        self.cont_size = cont_size
        self.image = pygame.image.load("Space/hangar.png").convert()
        self.rect = self.image.get_rect()
        self.rect.move_ip(cont_size[0]-100,cont_size[1]-700)
        
class Fabrica_de_robots(Recursos,sprite):
    def __init__(self,cont_size,nombre="FabricadeRobots"):
        Recursos.__init__(self,nombre)
        sprite.__init__(self)
        self.cont_size = cont_size
        self.image = pygame.image.load("Space/factory.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(cont_size[0]-100,cont_size[1]-550)


        