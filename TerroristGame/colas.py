class Nodo:

    def __init__(self,info):
        self.info=info
        self.sig=None

class Cola:

    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.tam=0

    def insertar(self, x):
        nuevo=Nodo(x)
        if self.cabeza==None:
            self.cabeza=nuevo
            self.cola=nuevo
            self.tam+=1
            return True
        self.cola.sig=nuevo
        self.cola=nuevo
        self.tam+=1
        return True
        
    
    def eliminar(self,n=0):
        x=None
        if self.cabeza==None:
            print("no hay elementos")
            return None
        elif n==0:
            x=self.cabeza
            self.cabeza=x.sig
            
        else:
            for i in range(n):
                x=x.sig

        self.tam-=1
        return x.info
    
    def es_vacia(self):
        return self.cabeza==None