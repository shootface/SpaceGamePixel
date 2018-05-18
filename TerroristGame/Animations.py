import pygame,sys
from pygame.locals import *
from random import randint
# Definimos algunos colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
pygame.init()
ventana = pygame.display.set_mode((1000,800))
pygame.display.set_caption("DesertAtack")
#Instanciacion imagenes juego
#Fondo
Space_imageBackground = pygame.image.load("Space/Space.jpg").convert()
#Ataques
nave_image = pygame.image.load("Space/nave.png").convert()
nave_image.set_colorkey(BLANCO)
#Personaje principal
principal_image = pygame.image.load("Space/principal.png").convert()
#Planetas
planet1_image = pygame.image.load("Space/planeta1.jpg").convert()
planet1_image.set_colorkey(BLANCO)
#Variables de control
velocidad = 5
Principal_posX = 500
Principal_posY = 720
Nave_posX = 0
Nave_posY = 0 
#Metodos de control '
def ataqueNave():
    print("Si llamo")
    Nave_posX = Principal_posX
    Nave_posY = Principal_posY-10
    ventana.blit(nave_image,(Nave_posX,Nave_posY))
while True:
    ventana.blit(Space_imageBackground,(0,0))
    ventana.blit(principal_image,(Principal_posX,Principal_posY))
    ventana.blit(planet1_image,(50,60))
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    Principal_posX -= velocidad
                elif event.key == K_RIGHT:
                    Principal_posX += velocidad
                elif event.key == K_z:
                    ataqueNave()
    print pygame.mouse.get_pos()
    pygame.display.update()

