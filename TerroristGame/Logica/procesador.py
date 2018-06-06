import threading
import colas as cola
import time
from quantum import Quantum


class Procesador(threading.Thread):
	def __init__(self,idProcesador,*args):
		threading.Thread.__init__(self)
		self.idProcesador=idProcesador
		self.proceso=None
		self.lisMax=cola.Cola()
		self.lisMed=cola.Cola()
		self.lisMin=cola.Cola()

		self.susMax=cola.Cola()
		self.susMed=cola.Cola()
		self.susMin=cola.Cola()

		self.bloMax=cola.Cola()
		self.bloMed=cola.Cola()
		self.bloMin=cola.Cola()

		self.ter=cola.Cola()
		self.blo=cola.Cola()
		self.sus=cola.Cola()
		self._args=args
		self.minIter=50
		self.uso=True
		self.ttotal=0

		self.quantum = Quantum()

	def __str__(self):
		return str(self.idProcesador)

	def run(self):
		while self.uso:
			self.usarProcesador(*self._args)

	def usarProcesador(self,q):
		self._args = q
		while not self.proceso==None or not q.empty() or not self.lisMin.es_vacia() or not self.lisMed.es_vacia() or not self.lisMax.es_vacia() or not self.susMin.es_vacia() or not self.susMed.es_vacia() or not self.susMax.es_vacia() or not self.bloMin.es_vacia() or not self.bloMed.es_vacia() or not self.bloMax.es_vacia() or self.minIter>0:
			time.sleep(1) #Tiempo de espera para la animacion del sprite
			self.minIter-=1
			self.lisMed.ordenar()
			if not q.empty():
				nuevo=q.get()
				self.asignar(nuevo)
				self.ttotal+=nuevo.t
				print(self.ttotal)

			if not self.lisMax.es_vacia() and self.proceso==None: #si la lista 1 no esta vacia y si el procesador no tiene proceso
				print("entro a max1")
				posible=self.lisMax.desencolar()
				if posible.recurso.libre:
					self.ocupado=True
					self.proceso=posible
					self.proceso.recurso.libre=False
					self.proceso.estado=3
					print("entro a asignar de la lista de maxima prioridad")
				else:
					self.bloMax.encolar(posible)
					posible.bloqueado()

			elif not self.lisMax.es_vacia() and not self.proceso==None and self.proceso.prioridad>0: #si la lista 1 no esta vacia, el procesador tiene proceso y el proceso tiene prioridad>0
				print("entro a max2")
				posible=self.lisMax.desencolar()
				if posible.recurso.libre:
					self.proceso.suspendido()
					print("entro a asignar de la lista de maxima prioridad cuando habia algo de menor prioridad")

					if self.proceso.prioridad==1:
						self.susMed.encolar(self.proceso)
					else:
						self.susMin.encolar(self.proceso)
					self.proceso=posible
					self.proceso.recurso.utilizar()
				else:
					self.lisMax.encolar(posible)

			elif not self.lisMed.es_vacia() and self.proceso==None and self.susMax.es_vacia() and self.bloMax.es_vacia():
				print("ENTRO A MEDIO")
				posible=self.lisMed.desencolar()
				print(posible)
				if posible.recurso.libre:
					print("entro a asignar de la lista de media prioridad")
					self.ocupado=True
					self.proceso=posible
					print("Asigna el recuro USANDO")
					self.proceso.recurso.utilizar()
					self.proceso.estado=3
				else:
					self.bloMed.encolar(posible)
					print("EN LISTA MEDIA ESTA BLOQUEANDO EL PROCESO")
					posible.bloqueado()

			elif not self.lisMed.es_vacia() and not self.proceso==None and self.susMax.es_vacia() and self.bloMax.es_vacia() and self.lisMax.es_vacia() and not self.proceso.prioridad==0:
				posible=self.lisMed.desencolar()
				#print("entro.... posible",posible,"prioridad",posible.prioridad,"actual",self.proceso,"prioridad",self.proceso.prioridad)
				if self.proceso.t>posible.t and posible.recurso.libre and self.proceso.prioridad==posible.prioridad:
					#print("entro a asignar de la lista de media prioridad cuando habia algo de menor tiempo")
					self.proceso.suspendido()
					self.susMin.encolar(self.proceso)
					self.proceso=posible
					self.proceso.recurso.utilizar()
				elif posible.recurso.libre and self.proceso.prioridad>posible.prioridad:
					#print("entro a asignar de la lista de media prioridad cuando habia algo de menor prioridad")
					self.proceso.suspendido()
					self.susMin.encolar(self.proceso)
					self.proceso=posible
					self.proceso.recurso.utilizar()
				else:
					self.lisMed.encolar(posible)


			elif not self.lisMin.es_vacia() and self.proceso==None and self.susMed.es_vacia() and self.bloMed.es_vacia() and self.susMax.es_vacia() and self.bloMax.es_vacia():
				posible=self.lisMin.desencolar()
				if posible.recurso.libre:
					print("entro a asignar de la lista de minima prioridad")
					self.ocupado=True
					self.proceso=posible
					self.proceso.recurso.libre=False
					self.proceso.estado=3
				else:
					self.bloMin.encolar(posible)
					posible.bloqueado()

			self.contarColaBlo()
			self.contarColaLis()
			self.revisarColaSus()
			self.revisarColaBlo()

			if not self.proceso==None:
    				print("PREPARANDO PARA PROCESAR")
				self.proceso.procesar()
				self.ttotal-=1
				#print(self.proceso,"quantum",self.proceso.quantum)
				if self.proceso.prioridad==0 and self.proceso.t>0 and self.proceso.quantum==0:
					self.susMax.encolar(self.proceso)
					self.proceso.suspendido()
					self.proceso=None
				elif self.proceso.t==0:
					self.proceso.recurso.liberar()
					self.proceso.estado=4
					self.ter.encolar(self.proceso)
					self.proceso=None
					q.task_done()

		print("termino el procesador",self,"lista de tareas completadas en este procesador:")
		for i in range(self.ter.tam):
			print(self.ter.desencolar())
		self.uso=False


	def revisarColaSus(self):
		tam = self.susMax.tam
		for i in range(tam):
			n=self.susMax.desencolar()
			n.tr-=1
			n.sus+=1
			if n.tr==0:
				self.asignar(n)
#				print("\nse saco el proceso",n,"de la cola de suspendidos y entro a la cola de listo")
			else:
				self.susMax.encolar(n)

		tam = self.susMed.tam
		for i in range(tam):
			n=self.susMed.desencolar()
			n.tr-=1
			n.sus+=1
			if n.tr==0:
				self.asignar(n)
#				print("\nse saco el proceso",n,"de la cola de suspendidos y entro a la cola de listo")
			else:
				self.susMed.encolar(n)

		tam = self.susMin.tam
		for i in range(tam):
			n=self.susMin.desencolar()
			n.tr-=1
			n.sus+=1
			if n.tr==0:
				self.asignar(n)
#				print("\nse saco el proceso",n,"de la cola de suspendidos y entro a la cola de listo")
			else:
				self.susMin.encolar(n)

	def revisarColaBlo(self):
		for i in range(self.bloMax.tam):
			posible=self.bloMax.desencolar()
			if posible.recurso.libre:
				self.asignar(posible)
#				print("\nse saco el proceso",posible," de la cola de bloqueados y entro en la cola de listos")
			else:
				self.bloMax.encolar(posible)

		for i in range(self.bloMed.tam):
			posible=self.bloMed.desencolar()
			if posible.recurso.libre:
				self.asignar(posible)
#				print("\nse saco el proceso",posible," de la cola de bloqueados y entro en la cola de listos")
			else:
				self.bloMed.encolar(posible)

		for i in range(self.bloMin.tam):
			posible=self.bloMin.desencolar()
			if posible.recurso.libre:
				self.asignar(posible)
#				print("\nse saco el proceso",posible," de la cola de bloqueados y entro en la cola de listos")
			else:
				self.bloMin.encolar(posible)

	def contarColaLis(self):
		tam = self.lisMax.tam
		for i in range(tam):
			n=self.lisMax.desencolar()
			n.lis+=1
			self.lisMax.encolar(n)

		tam = self.lisMed.tam
		for i in range(tam):
			n=self.lisMed.desencolar()
			n.lis+=1
			if n.te==0:
				self.lisMax.encolar(n)
				n.prioridad=0
				print("cambiando de prioridad a prioridad maxima   ",n)
			else:
				n.te-=1
				self.lisMed.encolar(n)

		tam = self.lisMin.tam
		for i in range(tam):
			n=self.lisMin.desencolar()
			n.lis+=1
			if n.te==0:
				print("cambiando de prioridad a prioridad media    ",n)
				n.prioridad=1
				n.asignarTiempoEnvejecimiento(self.ttotal)
				self.lisMed.encolar(n)
			else:
				n.te-=1
				self.lisMin.encolar(n)

	def contarColaBlo(self):
		tam = self.bloMax.tam
		for i in range(self.bloMax.tam):
			n=self.bloMax.desencolar()
			n.blo+=1
			self.bloMax.encolar(n)

		tam = self.bloMed.tam
		for i in range(self.bloMed.tam):
			n=self.bloMed.desencolar()
			n.blo+=1
			self.bloMed.encolar(n)

		tam = self.bloMin.tam
		for i in range(self.bloMin.tam):
			n=self.bloMin.desencolar()
			n.blo+=1
			self.bloMin.encolar(n)

	def asignar(self,proceso):
		proceso.estado=0
		if proceso.prioridad==0:
			proceso.quantum = self.quantum.asignarQ(proceso, self.lisMax, self._args)
			self.lisMax.encolar(proceso)
		elif proceso.prioridad==1:
			proceso.asignarTiempoEnvejecimiento(self.ttotal)
			self.lisMed.encolar(proceso)
		else:
			proceso.asignarTiempoEnvejecimiento(self.ttotal)
			self.lisMin.encolar(proceso)


""" class Procesador(threading.Thread):
	def __init__(self,idProcesador,args):
		threading.Thread.__init__(self)
		self.idProcesador=idProcesador
		self.proceso=None
		self.lis=cola.Cola()
		self.ter=cola.Cola()
		self.blo=cola.Cola()
		self.sus=cola.Cola()
		self._args=args
		self.uso=True
		self.ttotal=0
		self.minIter=50
		self.quantum = Quantum()

	def __str__(self):
		return str(self.idProcesador)

	def run(self):
		while self.uso:
			self.usarProcesador(self._args)

	def usarProcesador(self,q):
		self._args = q
        #mientras haya algo por ejecutar
		while not self.proceso==None or not q.empty() or not self.lis.es_vacia() or not self.sus.es_vacia() or not self.blo.es_vacia() or self.minIter>0:
			time.sleep(1.5) #tiempo para cada accion en el procesador
			self.minIter-=1
			if not q.empty():
				nuevo=q.get()
				self.asignar(nuevo)
				self.ttotal+=nuevo.t
			if not self.lis.es_vacia() and self.proceso==None:
				posible=self.lis.desencolar()
				print "el tiempo del proceso desencolado es" , posible.t
				if posible.recurso.libre:
					self.ocupado=True
					self.proceso=posible
					self.proceso.recurso.libre=False
					self.proceso.estado=3
					print("\ncomenzando proceso",self.proceso,"en el procesador",self)
				else:
					print("\nel proceso",posible.nombre,"requiere de un recurso ocupado, encolando en bloqueado")
					self.blo.encolar(posible)
					posible.estado=1
					posible.bloqueado()

			self.contarColaBlo()
			self.contarColaLis()
			self.revisarColaSus()
			self.revisarColaBlo()

			if not self.proceso==None: #si hay un proceso en el procesador se procesa
				self.proceso.procesar()
				print("procesador",self.idProcesador,"con",self.proceso.nombre)
				self.ttotal-=1
				if self.proceso.t>0 and self.proceso.quantum==0: #si el proceso no ha terminado y se ha agotado el quantum
					self.proceso.tr=5
					self.proceso.recurso.libre=True
					self.sus.encolar(self.proceso)
					self.proceso.estado=2
					self.proceso.suspendido()
					print("\nse reencolo el proceso",self.proceso,"a suspendidos")
					self.proceso=None
				elif self.proceso.t==0: #si el proceso ya termino se despacha
					self.proceso.recurso.libre=True
					print("\nterminando proceso",self.proceso,"en el procesador",self,",sus",self.proceso.sus,",lis",self.proceso.lis,",blo",self.proceso.blo,",zona critica",self.proceso.zc)
					self.ter.encolar(self.proceso)
					self.proceso.estado=4
					self.proceso=None
					q.task_done()
		print("termino el procesador",self,"lista de tareas completadas en este procesador:")
		for i in range(self.ter.tam):
			print(self.ter.desencolar())
		self.uso=False


	def revisarColaSus(self):
		tam = self.sus.tam
		for i in range(tam):
			n=self.sus.desencolar()
			n.tr-=1
			n.sus+=1
			if n.tr==0:
				print("\nse saco el proceso",n.nombre, n.idProceso,"de la cola de suspendidos y entro a la cola de listo")
				self.asignar(n)
			else:
				self.sus.encolar(n)

	def revisarColaBlo(self):
		for i in range(self.blo.tam):
			posible=self.blo.desencolar()
			if posible.recurso.libre:
				self.asignar(posible)
				print("\nse saco el proceso",posible," de la cola de bloqueados y entro en la cola de listos")
			else:
				self.blo.encolar(posible)

	def contarColaLis(self):
		tam = self.lis.tam

		for i in range(tam):
			n=self.lis.desencolar()
			n.lis+=1
			self.lis.encolar(n)


	def contarColaBlo(self):
		tam = self.blo.tam
		for i in range(self.blo.tam):
			n=self.blo.desencolar()
			n.blo+=1
			self.blo.encolar(n)

	def asignar(self,proceso):
		self.lis.encolar(proceso)
		quan = self.quantum.asignarQ(proceso, self.lis, self._args)
		proceso.quantum = quan
		#print "el t del proceso es", proceso.t ,"y el quantum es", quan
		proceso.estado=0 """