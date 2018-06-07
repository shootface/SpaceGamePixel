class Recursos:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libre=True
    
    def __str__(self):
        return(self.nombre)
    
    def utilizar(self):
        if self.libre:
            print("Usando el",self.nombre)
            self.libre = False
        else:
            print("el",self.nombre,"esta ocupado")
    def liberar(self):
        if not self.libre:
            print("el",self.nombre,"fue liberado")
            self.libre=True
        else:
            print("el",self.nombre,"no estaba siendo usado")