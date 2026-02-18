#TECNOLÓGICO NACIONAL DE MÉXICO CAMPUS SAN JUAN DEL RÍO 
#Ingeniería en Sistemas Computacionales
#CLASE GENERICA PARA LA GESTION DE ARBOLES
#Autor: Hugo Francisco Martinez Briseño
#Versión 1.0

class ArbolBB:
	
#--------------------- VARIABLES MIEMBRO ---------------------#
	listABB = "\n "
	x = ""

#--------------------- CONSTRUCTOR ---------------------#
	def __init__(self,dato,direc1,direc2):
		self.info = dato
		self.izq = direc1
		self.der = direc2

#--------------------- CABECERA ---------------------#
	def crea_cab(self):
		self.P = ArbolBB(None,None,None)

#--------------------- CRACIÓN DE NODOS ---------------------#
	def crea_nodo(self):
		self.nuevo = ArbolBB(None,None,None)

#--------------------- CREACIÓN / INSERCIÓN ---------------------#
	def insertar(self,tipo):
		self.crea_nodo()
		valido = False
		while not valido:
			try:
				self.nuevo.info = tipo(input("\n Ingrese el valor a insertar -> "))
				valido = True
			except ValueError:
				print("\n ¡ERROR! Por favor ingrese un valor numérico válido.\n")
		
		if self.P.izq == None:
			self.P.izq = self.nuevo
		else:
			Q = self.P.izq
			ban = True
			while ban:
				if self.nuevo.info <= Q.info:
					if Q.izq == None:
						Q.izq = self.nuevo
						ban = False
					else:
						Q = Q.izq
				elif Q.der == None:
					Q.der = self.nuevo
					ban = False
				else:
					Q = Q.der

#--------------------- IMPRIMIR / RECORRIDO ---------------------#
	def preorden(self,Q):
		if Q != None:
			self.listABB += " "+str(Q.info)
			self.preorden(Q.izq)
			self.preorden(Q.der)
	
	def inorden(self,Q):
		if Q != None:
			self.inorden(Q.izq)
			self.listABB += " "+str(Q.info)
			self.inorden(Q.der)
	
	def postorden(self,Q):
		if Q != None:
			self.postorden(Q.izq)
			self.postorden(Q.der)
			self.listABB += " "+str(Q.info)

#--------------------- ELIMINACIÓN ---------------------#
	def elimina1(self):
		if self.P.izq == None:
			print("\n  ¡¡Árbol vacío!!\n")
		else:
			self.b = 0
			x = int(input("\n Ingresa el dato a eliminar ---> "))
			Q = self.P.izq
			if Q.info == x:
				self.P.izq = self.elimina2(self.P.izq)
				self.b = 1
			else:
				T = Q
				#self.b = 1
				while self.b == 0 and Q != None:
					if x == Q.info:
						if Q.info < T.info:
							T.izq = self.elimina2(T.izq)
							self.b = 1
						else:
							T.der = self.elimina2(T.der)
							self.b = 1
					else:
						T = Q
						if x < Q.info:
							Q = Q.izq
						else:
							Q = Q.der
			if self.b == 0:
				print("\n ¡¡No existe ese dato!!\n\n")
			else:
				print(f"\n ¡El dato {x} fue eliminado!\n")
	
	def elimina2(self,R):
		if R == None:
			print("\n ¡¡No existe ese dato!!\n")
		else:
			n = R
			if R.der == None:
				R = R.izq
			elif R.izq == None:
				R = R.der
			else:
				n = R.der
				while n.izq != None:
					n = n.izq
				n.izq = R.izq
				n = R
				R = R.der
			n = None
		return R

#--------------------- BÚSQUEDA ---------------------#
	def buscar(self,Q): #recorriendo en preorden
		if Q != None and self.b == 0:
			if Q.info == self.x:
				print(f"\n El dato {self.x} si existe en el ABB\n")
				self.b = 1
			self.buscar(Q.izq)
			self.buscar(Q.der)
