

class espacio(Sprite):
    def __init__(self,posX=0,posY=0,nombre="espacio"):
        Sprite.__init__(self)
        self.images = list()        
        self.rect.left = posX
        self.rect.top = posY

    def cargarImagenes(self):
        for i in range(73):
            str = i + '.gif'
            self.images.append(pygame.image.load("Space/espacioGIF/"+str))
    
    def dibujar(self,ventana):
        for j in range(73):
            ventana.blit(self.images[j],(0,0))