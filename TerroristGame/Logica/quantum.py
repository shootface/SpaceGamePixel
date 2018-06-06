import copy

class Quantum ():

    def __init__(self):
        self.lisProcesos1 = list()
    
    def actualizarValores(self, colaLis, colaQ):
        self.lisProcesos1 = list()
        colaLisCopy = copy.deepcopy(colaLis) 
        colaQCopy = list(colaQ.queue)
        tam = colaLisCopy.tam
        print 'el tamano de cola lis es ', tam
        print 'el tamano de colaq es' , len(colaQCopy)

        for i in range(tam):
            n = colaLisCopy.desencolar()
            self.lisProcesos1.append(n)

        for pro in colaQCopy:
            self.lisProcesos1.append(pro)

    def asignarQ(self, proceso, colaLis, colaQ):
        self.actualizarValores(colaLis, colaQ)
        print ("se tienen" , len(self.lisProcesos1), "procesos en total")
        #print "en asignarq el proceso tiene t=" , proceso.t
        mean = 0
        mediana = 0

        if len(self.lisProcesos1) > 1:
            # se ordena por tiempo de ejecucion los procesos
            self.lisProcesos1.sort(key=lambda proceso: proceso.t)

            if len(self.lisProcesos1) % 2 == 0:
                n = len(self.lisProcesos1)
                # se halla la mediana
                mediana = (self.lisProcesos1[n / 2 - 1].t + self.lisProcesos1[n / 2].t) / 2
                #print "en asignarq  mod 2 el proceso tiene t=" , proceso.t
            else:
                mediana = self.lisProcesos1[len(self.lisProcesos1) / 2].t
                #print "en asignarq el mod 1 proceso tiene t=" , proceso.t

            for procesos in self.lisProcesos1:
                mean = mean + procesos.t  # se halla la media
            mean = mean / len(self.lisProcesos1)

            quantum = (mean + mediana)/2

            if quantum >= proceso.t :
                quantum = int(quantum - 0.45*proceso.t)-1

            #print "el quantum es ", quantum, "el tiempo del proceso es", proceso.t

            return quantum
        else:
            return proceso.t
