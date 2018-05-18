import threading
import cola

class Procesador(threading.Thread):
	def __init__(self,idProcesador,*args):
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

	def __str__(self):
		return str(self.idProcesador)

	def run(self):
		while self.uso:
			self.usarProcesador(*self._args)

	def usarProcesador(self,q):
        #mientras haya algo por ejecutar
		while not self.proceso==None or not q.empty() or not self.lis.es_vacia() or not self.sus.es_vacia() or not self.blo.es_vacia() or self.minIter>0:
			time.sleep(2.5) #tiempo para cada accion en el procesador
			self.minIter-=1
			if not q.empty():
				nuevo=q.get()
				self.asignar(nuevo)
				self.ttotal+=nuevo.t
			if not self.lis.es_vacia() and self.proceso==None:
				posible=self.lis.desencolar()
				if posible.recurso.libre:
					self.ocupado=True
					self.proceso=posible
					self.proceso.recurso.libre=False
					self.proceso.estado=3
#					print("\ncomenzando proceso",self.proceso,"en el procesador",self)
				else:
#					print("\nel proceso",posible,"requiere de un recurso ocupado, encolando en bloqueado")
					self.blo.encolar(posible)
					posible.estado=1

			self.contarColaBlo()
			self.contarColaLis()
			self.revisarColaSus()
			self.revisarColaBlo()

			if not self.proceso==None: #si hay un proceso en el procesador se procesa
				self.proceso.procesar()
				print("procesador",self,"con",self.proceso)
				self.ttotal-=1
				if self.proceso.t>0 and self.proceso.quantum==0: #si el proceso no ha terminado y se ha agotado el quantum
					self.proceso.tr=5
					self.proceso.recurso.libre=True
					self.sus.encolar(self.proceso)
					self.proceso.estado=2
#					print("\nse reencolo el proceso",self.proceso,"a suspendidos")
					self.proceso=None
				elif self.proceso.t==0: #si el proceso ya termino se despacha
					self.proceso.recurso.libre=True
#					print("\nterminando proceso",self.proceso,"en el procesador",self,",sus",self.proceso.sus,",lis",self.proceso.lis,",blo",self.proceso.blo,",zona critica",self.proceso.zc)
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
				self.asignar(n)
#				print("\nse saco el proceso",n,"de la cola de suspendidos y entro a la cola de listo")
			else:
				self.sus.encolar(n)

	def revisarColaBlo(self):
		for i in range(self.blo.tam):
			posible=self.blo.desencolar()
			if posible.recurso.libre:
				self.asignar(posible)
#				print("\nse saco el proceso",posible," de la cola de bloqueados y entro en la cola de listos")
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
		proceso.quantum=proceso.asignarQ(self.ttotal)
		proceso.estado=0
		self.lis.encolar(proceso)