import copy

class Quantum ():

    def __init__(self):
        self.lisProcesos1 = list()
    
    def actualizarValores(self, colaLis):
        colaLisCopy = copy.deepcopy(colaLis) 
        tam = colaLisCopy.tam

        for i in range(tam):
            n = colaLisCopy.desencolar()
            self.lisProcesos1.append(n)


    def asignarQ(self, proceso, cola):
        self.actualizarValores(cola)
        mean = 0
        mediana = 0
        if len(self.lisProcesos1) != 0:
            # se ordena por tiempo de ejecucion los procesos
            self.lisProcesos1.sort(key=lambda proceso: proceso.t)

            if len(self.lisProcesos1) % 2 == 0:
                n = len(self.lisProcesos1)
                # se halla la mediana
                mediana = (
                    self.lisProcesos1[n / 2 - 1].t + self.lisProcesos1[n / 2].t) / 2
            else:
                mediana = self.lisProcesos1[len(self.lisProcesos1) / 2].t

            for proceso in self.lisProcesos1:
                mean = mean + proceso.t  # se halla la media
            mean = mean / len(self.lisProcesos1)

            quantum = (mean + mediana)/2
            return quantum
        else:
            return 15
