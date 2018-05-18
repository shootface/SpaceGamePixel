import pygame,sys
from pygame.locals import *
from recursos import *
from principal import Principal
#Metodos de control 
"""def animacionInicio():
def ataqueNave():
    Nave_posX = Principal_posX
    Nave_posY = Principal_posY-100
    ventana.blit(nave_image,(Nave_posX,Nave_posY))
"""
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
    #Ejecucion animaciones
    while True:  
        ventana.blit(Space_imageBackground,(0,0))
        jugador.dibujar(ventana)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    movimiento()
                elif event.key == K_RIGHT:
                    movimiento(even)
                elif event.key == K_z:
                    ataqueNave()
        print pygame.mouse.get_pos()
        pygame.display.update()

SpaceAtack()