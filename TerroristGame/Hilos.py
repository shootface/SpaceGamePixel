# Libreria para el manejo de los hilos
import threading

from principal import Principal

# Definicion de clases
class NaveHilo(threading.Thread):
    # Funcion inicio del hilo
    
    def __init__(self, jugador,ventana):  
        threading.Thread.__init__(self)  
        self.jugador = jugador
        self.ventana = ventana
        self.stoprequest = threading.Event()
    
    def run(self):
        
