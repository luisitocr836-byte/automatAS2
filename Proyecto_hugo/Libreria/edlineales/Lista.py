#TECNOLÓGICO NACIONAL DE MÉXICO CAMPUS SAN JUAN DEL RÍO 
#Ingeniería en Sistemas Computacionales
#CLASE GENERICA PARA LA GESTION DE PILAS
#Autor: Hugo Francisco Martinez Briseño
#Versión 1.0

class Lista:
	
	#------------------------- VARIABLES MIEMBRO -------------------------#
	existen = 0 # <---------- AGREGAR
	existenLSC = 0
	existenLDL = 0
	existenLDC = 0
	
	#------------------------- CONSTRUCTOR -------------------------#
	"""
	def __init__(self,dato,direc):
		self.info = dato
		self.sig = direc
	"""
	def __init__(self, *args):
		self.info = ""
		self.sig = None
		if len(args) == 3:
			self.ant = None
	
	#------------------------- CABECERA -------------------------#
	def crea_cab_LSL(self):
		self.P = Lista("",None)
	
	def crea_cab_LSC(self):
		self.P = Lista("", None)
		self.P.sig = self.P
	
	def crea_cab_LDL(self):
		self.P = Lista("", None, None)
	
	def crea_cab_LDC(self):
		self.P = Lista("",None)
		self.P.sig = self.P
		self.P.ant = self.P
	
	#------------------------- CREACIÓN DE NODOS -------------------------#
	def crea_nodo_LS(self):
		self.nuevo = Lista("",None)
	
	def crea_nodo_LD(self):
		self.nuevo = Lista("",None,None)
	
	#         * * *  S I M P L E   L I N E A L  * * *
	#------------------------- CREACIÓN/INSERCIÓN AL INICIO -------------------------#
	def crea_ins_ini_LSL(self):
		self.crea_nodo_LS()
		self.nuevo.info = input("\n  Ingrese el daro a insertar ---> ")
		self.nuevo.sig = self.P.sig
		if self.P.sig == None:
			self.F = self.nuevo
		
		self.P.sig = self.nuevo
		self.existen += 1 # <--- AGREGAR
	
	#------------------------- CRACIÓN/INSERCIÓN AL FINAL -------------------------#
	def crea_ins_fin_LSL(self):
		self.crea_nodo_LS()
		self.nuevo.info = input("\n  Ingrese el dato a insertar ---> ")
		
		if self.P.sig == None:
			self.P.sig = self.nuevo
		else:
			self.F.sig = self.nuevo
		
		self.F = self.nuevo
		self.existen += 1 # <--- AGREGAR
	 
	#------------------------- IMPRIMIR / RECORRIDO -------------------------#
	def recorre_LSL(self):
		if self.P.sig != None:
			listLS = "\n  P ->"
			if self.P.sig == self.F:
				listLS +=" "+self.F.info+" ->"
			else:
				Q = self.P.sig
				while(Q != None):
					listLS += " "+Q.info+" ->"
					Q = Q.sig
			listLS +=" null"
			print(listLS)
		else:
			print("\n\n  P -> null     ¡¡Lista Vacía!!\n\n")
	
	#------------------------- BUSCAR -------------------------#
	def buscar_LSL(self):
		if self.P.sig != None:
			X = input("\n    Igrese el dato a buscar ---> ")
			listLS = "\n  P ->"
			if self.F.info == X:
				print("\n\n  "+X+" Si existe\n\n")
			elif self.P.sig == self.F:
				print("\n\n  ¡"+X+" NO existe!\n\n")
			else:
				Q = self.P.sig
				#while (Q != None)and(Q.info != X):
				while (Q != None)and(Q.info != X):
					Q = Q.sig
				if Q != None:
					print("\n\n  "+X+" Si existe\n\n")
				else:
					print("\n\n  ¡"+X+" NO existe!\n\n")
		else:
			print("\n\n  P -> null    ¡¡Lista Vacía!!\n\n")
	
	#------------------------- INSERTAR EN LUGAR ESPECIFÍCO -------------------------#
	def insertaSitioX_LSL(self):
		if self.P.sig == None:
			self.crea_ins_ini_LSL()
		else:
			lugar = int(input("\n No. de lugar o sitio a insertar ---> "))
			if lugar <= 0:
				print("\n  ERROR...No. de sitio incorrecto!!")
			elif lugar == 1:
				self.crea_ins_ini_LSL()
			elif lugar > self.existen:
				print(f"\n  Sólo existen {self.existen} nodos...Se insertará al final")
				self.crea_ins_fin_LSL()
			else:
				self.crea_nodo_LS() #creacion del nodo
				self.nuevo.info = input("\n   Dato a insertar ---> ")
				Q = self.P.sig
				sitio = 1
				while lugar != sitio:
					T = Q
					Q = Q.sig
					sitio += 1
				T.sig = self.nuevo
				self.nuevo.sig = Q
				self.existen += 1
	
	#------------------------- ELIMINAR POR INFO -------------------------#
	def eliminaInfo_LSL(self):
		if self.P.sig != None:
			X = input("\n    Ingrese el valor del nodo a eliminar ---> ")
			if self.P.sig == self.F:
				if self.F.info == X:
					self.P.sig = None
					self.F = None
					self.existen -= 1
				else:
					print(f"\n  ¡¡No existe el dato {X}!!\n")
			else:
				Q = self.P.sig
				while(Q != None)and(Q.info != X):
				#while(Q.info != X)and(Q != None):
					T = Q
					Q = Q.sig
				if Q == None:
					print(f"\n   ¡¡No existe el dato {X}!!\n")
				else:
					if self.P.sig == Q:
						self.P.sig = Q.sig
					else:
						T.sig = Q.sig
						if Q == self.F:
							self.F = T
					Q = None
					self.existen -= 1
					print(f"\n  ¡¡El dato {X} fue eliminado!!\n")
		else:
			print("\n\n  P -> null    ¡¡Lista Vacía!!\n\n")
	
	#------------------------- ELIMINAR POR No. NODO -------------------------#
	def eliminarNoNodo_LSL(self):
		if self.P.sig != None:
			lugar = int(input("\n   ¿Cuál es el número del nodo a eliminar? ---> "))
			if lugar <= 0:
				print("\n   ¡¡ERROR!!!...No. de nodo incorrecto!!!\n")
			elif lugar > self.existen:
				print("\n   ¡¡No. de nodo superior a los que existen!!\n")
			elif self.P.sig == self.P:
				self.P.sig = None
				self.F = None
				self.existen -= 1
			else:
				Q = self.P.sig
				sitio = 1
				while sitio != lugar:
					T = Q
					Q = Q.sig
					sitio += 1
				if self.P.sig == Q:
					self.P.sig = Q.sig
				else:
					T.sig = Q.sig
					if Q == self.F:
						self.F = T
				print(f"\n   ¡¡El nodo no. {lugar} que contiene el dato: {Q.info} fue eliminado!!\n")
				Q = None
				self.existen -= 1
		else:
			print("\n\n  P -> null    ¡¡Lista Vacía!!\n\n")

	#         * * *  S I M P L E   C I R C U L A R  * * *
	#------------------------- CREACIÓN/INSERCIÓN AL INICIO -------------------------#
	def crea_ins_ini_LSC(self):
		self.crea_nodo_LS()
		self.nuevo.info = input("\n  Ingrese el daro a insertar ---> ")
		self.nuevo.sig = self.P.sig
		if self.P.sig == self.P:
			self.F = self.nuevo
		
		self.P.sig = self.nuevo
		self.existenLSC += 1 # <--- AGREGAR

	#------------------------- CREACIÓN/INSERCIÓN AL FINAL -------------------------#
	def crea_ins_fin_LSC(self):
		self.crea_nodo_LS()
		self.nuevo.info = input("\n  Ingrese el dato a insertar ---> ")
		self.nuevo.sig = self.P
		
		if self.P.sig == self.P:
			self.P.sig = self.nuevo
		else:
			self.F.sig = self.nuevo
		
		self.F = self.nuevo
		self.existenLSC += 1 # <--- AGREGAR

	#------------------------- IMPRIMIR / RECORRIDO -------------------------#
	def recorre_LSC(self):
		if self.P.sig != self.P:
			listLS = "\n  P ->"
			if self.P.sig == self.F:
				listLS +=" "+self.F.info+" ->"
			else:
				Q = self.P.sig
				while(Q != self.P):
					listLS += " "+Q.info+" ->"
					Q = Q.sig
			listLS +=" P"
			print(listLS)
		else:
			print("\n\n  P -> P     ¡¡Lista Vacía!!\n\n")

	#------------------------- BUSCAR -------------------------#
	def buscar_LSC(self):
		if self.P.sig != self.P:
			X = input("\n    Igrese el dato a buscar ---> ")
			listLS = "\n  P ->"
			if self.F.info == X:
				print("\n\n  "+X+" Si existe\n\n")
			elif self.P.sig == self.F:
				print("\n\n  ¡"+X+" NO existe!\n\n")
			else:
				Q = self.P.sig
				#while (Q != None)and(Q.info != X):
				while (Q != self.P)and(Q.info != X):
					Q = Q.sig
				if Q != self.P:
					print("\n\n  "+X+" Si existe\n\n")
				else:
					print("\n\n  ¡"+X+" NO existe!\n\n")
		else:
			print("\n\n  P -> P    ¡¡Lista Vacía!!\n\n")
	
	#------------------------- INSERTAR EN LUGAR ESPECIFÍCO -------------------------#
	def insertaSitioX_LSC(self):
		if self.P.sig == self.P:
			self.crea_ins_ini_LSC()
		else:
			lugar = int(input("\n No. de lugar o sitio a insertar ---> "))
			if lugar <= 0:
				print("\n  ERROR...No. de sitio incorrecto!!")
			elif lugar == 1:
				self.crea_ins_ini_LSC()
			elif lugar > self.existenLSC:
				print(f"\n  Sólo existen {self.existenLSC} nodos...Se insertará al final")
				self.crea_ins_fin_LSC()
			else:
				self.crea_nodo_LS() #creacion del nodo
				self.nuevo.info = input("\n   Dato a insertar ---> ")
				Q = self.P.sig
				sitio = 1
				while lugar != sitio:
					T = Q
					Q = Q.sig
					sitio += 1
				T.sig = self.nuevo
				self.nuevo.sig = Q
				self.existenLSC += 1

	#------------------------- ELIMINAR POR INFO -------------------------#
	def eliminaInfo_LSC(self):
		if self.P.sig != self.P:
			X = input("\n    Ingrese el valor del nodo a eliminar ---> ")
			if self.P.sig == self.F:
				if self.F.info == X:
					self.P.sig = self.P
					self.F = None
					self.existenLSC -= 1
				else:
					print(f"\n  ¡¡No existe el dato {X}!!\n")
			else:
				Q = self.P.sig
				while(Q != self.P)and(Q.info != X):
				#while(Q.info != X)and(Q != None):
					T = Q
					Q = Q.sig
				if Q == self.P:
					print(f"\n   ¡¡No existe el dato {X}!!\n")
				else:
					if self.P.sig == Q:
						self.P.sig = Q.sig
					else:
						T.sig = Q.sig
						if Q == self.F:
							self.F = T
					Q = None
					self.existenLSC -= 1
					print(f"\n  ¡¡El dato {X} fue eliminado!!\n")
		else:
			print("\n\n  P -> P    ¡¡Lista Vacía!!\n\n")

	#------------------------- ELIMINAR POR No. NODO -------------------------#
	def eliminarNoNodo_LSC(self):
		if self.P.sig != self.P:
			lugar = int(input("\n   ¿Cuál es el número del nodo a eliminar? ---> "))
			if lugar <= 0:
				print("\n   ¡¡ERROR!!!...No. de nodo incorrecto!!!\n")
			elif lugar > self.existenLSC:
				print("\n   ¡¡No. de nodo superior a los que existen!!\n")
			elif self.P.sig == self.F:
				self.P.sig = self.P
				self.F = None
				self.existenLSC -= 1
			else:
				Q = self.P.sig
				sitio = 1
				while sitio != lugar:
					T = Q
					Q = Q.sig
					sitio += 1
				if self.P.sig == Q:
					self.P.sig = Q.sig
				else:
					T.sig = Q.sig
					if Q == self.F:
						self.F = T
				print(f"\n   ¡¡El nodo no. {lugar} que contiene el dato: {Q.info} fue eliminado!!\n")
				Q = None
				self.existenLSC -= 1
		else:
			print("\n\n  P -> P    ¡¡Lista Vacía!!\n\n")
	
	#         * * *  D O B L E   L I N E A L  * * *
	#------------------------- CREACIÓN/INSERCIÓN AL INICIO -------------------------#
	def crea_ins_ini_LDL(self):
		self.crea_nodo_LD()
		self.nuevo.info = input("\n  Ingrese el dato a insertar ---> ")
		self.nuevo.sig = self.P.sig
		
		if self.P.sig == None:
			self.F = self.nuevo
		else:
			if self.P.sig == self.F:
				self.F.ant == self.nuevo
			else:
				Q = self.P.sig
				Q.ant = self.nuevo
		
		self.P.sig = self.nuevo
		self.nuevo.ant = self.P
		self.existenLDL += 1 # <--- AGREGAR
	
	#------------------------- CRACIÓN/INSERCIÓN AL FINAL -------------------------#
	def crea_ins_fin_LDL(self):
		self.crea_nodo_LD()
		self.nuevo.info = input("\n  Ingrese el dato a insertar ---> ")
		
		if self.P.sig == None:
			self.P.sig = self.nuevo
			self.nuevo.ant = self.P
		else:
			self.F.sig = self.nuevo
			self.nuevo.ant = self.F
		
		self.F = self.nuevo
		self.existenLDL += 1 # <--- AGREGAR
	
	#------------------------- IMPRIMIR / RECORRIDO -------------------------#
	#Recorrido de P - F, utilizar recorre_LSL()
	
	#Recorrido de F - P
	def recorre_LDL_FP(self):
		if self.P.sig != None:
			listLS = "\n  null <- P <->"
			if self.P.sig == self.F:
				listLS +=" "+self.F.info+" ->"
			else:
				Q = self.F
				while(Q != self.P):
					listLS += " "+Q.info+" ->"
					Q = Q.ant
			listLS +=" P -> null"
			print(listLS)
		else:
			print("\n\n  null <- P -> null     ¡¡Lista Vacía!!\n\n")
	
	#--------------------------- BUSCAR  --------------------------------#
	#De principio a final P a F, utilizar buscar_LSL()

	#De final a principio F a P
	def buscar_LDL_FP(self):
		if self.P.sig != None:
			X = input("\n Ingrese el dato a buscar -> ")
			if self.F.info == X:
				print("\n\n "+X+" si existe \n\n")
			elif self.P.sig == self.F:
				print("\n\n "+X+" no existe \n\n")
			else:
				Q = self.F.ant
				while (Q != self.P) and (Q.info != X):
					Q = Q.ant
				if Q != self.P:
					print("\n\n "+X+" si existe \n\n")
				else:
					print("\n\n "+X+" no existe \n\n")
		else:
			print("\n\n null <- P -> null ¡¡Lista vacía!! \n\n")

	#------------------------- Insertar en sitio específico ----------------------------------------# 
	def insertaSitioX_LDL(self):
		if self.P.sig == None:
			self.crea_ins_ini_LDL()
		else:
			lugar = int(input("\n No. de lugar o sitio a insertar -> "))
			if lugar <= 0:
				print("\n ¡¡Error!! No. de sitio incorrecto. ")
			elif lugar == 1:
				self.crea_ins_ini_LDL()
			elif lugar > self.existenLDL:
				print("\n Solo existen ",self.existenLDL," nodos... Se insertará al final. ") 
				self.crea_ins_fin_LDL()
			else:
				self.crea_nodo_LD() #Creación del nodo
				self.nuevo.info = input("\n Dato a insertar -> ")
				if lugar == self.existenLDL:
					T = self.F.ant
					self.F.ant = self.nuevo
				else:
					Q = self.P.sig
					sitio = 1
					while lugar != sitio:
						Q = Q.sig
						sitio += 1
					T = Q.ant
					Q.ant = self.nuevo
				self.nuevo.sig = T.sig
				T.sig = self.nuevo
				self.nuevo.ant = T
				self.existenLDL += 1 

	#----------------------------- Eliminación por info --------------------------------------------#
	def eliminaInfo_LDL(self):
		if self.P.sig != None:
			X = input("\n Ingrese el valor del nodo a eliminar -> ")
			if self.F.info == X:
				if self.P.sig == self.F:
					self.P.sig = None
					self.F = None
					self.existenLDL -= 1
				else:
					Q = self.F
					self.F = self.F.ant
					self.F.sig = None
			elif self.P.sig == self.F:
				print("\n ¡¡No existe el dato ",X,"!!\n")
			else:
				Q = self.P.sig
				while(Q != None) and (Q.info != X):
				#while(Q.info != X) and (Q != None):
					Q = Q.sig
				if Q == None:
					print("\n ¡¡No existe el dato ",X,"!!\n")
				else:
					if self.P.sig == Q:
						self.P.sig = Q.sig
					else:
						T = Q.ant
						T.sig = Q.sig
						if Q.sig == self.F:
							self.F.ant = Q.ant
						else:
							R = Q.sig
							R.ant = Q.ant
					Q = None
					self.existenLDL -= 1
					print("\n ¡¡El dato ",X," fue eliminado!! \n")
		else:
			print("\n\n null <- P -> null       ¡¡Lista Vacía!!\n\n")

	#----------------------------- Eliminación por No. de nodo --------------------------------------------#
	def eliminarNoNodo_LDL(self):
		if self.P.sig != None:
			lugar = int(input("\n ¿Cuál es el número o lugar del nodo a eliminar? "))
			if lugar <= 0:
				print("\n ¡¡Error!! No. de nodo incorrecto. ")
			elif lugar > self.existenLDL:
				print("\n ¡¡No. de nodo superior a los que existen!! \n")
			elif lugar == self.existenLDL:
				if self.P.sig == self.F:
					self.P.sig = None
					self.F = None
				else:
					Q = self.F
					self.F = self.F.ant
					self.F.sig = None
					Q = None
				self.existenLDL -= 1
			else:
				Q = self.P.sig
				sitio = 1
				while sitio != lugar:
					Q = Q.sig
					sitio += 1
				if self.P.sig == Q:
					self.P.sig = Q.sig
				else:
					T = Q.ant
					T.sig = Q.sig
					if Q.sig == self.F:
						self.F.ant = Q.ant
					else:
						R = Q.sig
						R.ant = Q.ant
				print("\n ¡¡El nodo No. ",lugar," que contiene el dato: ",Q.info," fue eliminado!!")
				Q = None
				self.existenLDL -= 1
		else:
			print("\n\n null <- P -> null       ¡¡Lista Vacía!!\n\n")
	
	#         * * *  D O B L E   C I R C U L A R  * * *
	#------------------------- CREACIÓN/INSERCIÓN AL INICIO -------------------------#
	def crea_ins_ini_LDC(self):
		self.crea_nodo_LD()
		self.nuevo.info = input("\n  Ingrese el dato a insertar ---> ")
		self.nuevo.sig = self.P.sig
		
		if self.P.sig == self.P:
			self.F = self.nuevo
			self.P.ant = self.nuevo
		elif self.P.sig == self.F:
			self.F.ant = self.nuevo
		else:
			Q = self.P.sig
			Q.ant = self.nuevo
		
		self.P.sig = self.nuevo
		self.nuevo.ant = self.P
		self.existenLDC += 1 # <--- AGREGAR
	
	#------------------------- CRACIÓN/INSERCIÓN AL FINAL -------------------------#
	def crea_ins_fin_LDC(self):
		self.crea_nodo_LD()
		self.nuevo.info = input("\n  Ingrese el dato a insertar ---> ")
		self.nuevo.sig = self.P
		self.P.ant = self.nuevo
		
		if self.P.sig == self.P:
			self.P.sig = self.nuevo
			self.nuevo.ant = self.P
		else:
			self.F.sig = self.nuevo
			self.nuevo.ant = self.F
		
		self.F = self.nuevo
		self.existenLDC += 1 # <--- AGREGAR
	
	#------------------------- IMPRIMIR / RECORRIDO -------------------------#
	#De pirncipio a final P a F, utilizar el algoritno recorre_LSC()
	
	#De final a principio F a P
	def recorre_LDC_FP(self):
		if self.P.sig != self.P:
			listLD = "\n  P <-"
			if self.P.sig == self.F:
				listLD +=" "+self.F.info+" <->"
			else:
				Q = self.F
				while(Q != self.P):
					listLD += " "+Q.info+" <->"
					Q = Q.ant
			listLD +=" P"
			print(listLD)
		else:
			print("\n\n  P <-> P     ¡¡Lista Vacía!!\n\n")
	
	#------------------------- BUSCAR -------------------------#
	#De pirncipio a final P a F, utilizar el algoritno buscar_LSC()
	
	#De final a principio F a P, utilizar el algoritmo buscar_LDL()
	
	#------------------------- INSERTAR EN LUGAR ESPECIFÍCO -------------------------#
	def insertaSitioX_LDC(self):
		if self.P.sig == self.P:
			self.crea_ins_ini_LDC()
		else:
			lugar = int(input("\n No. de lugar o sitio a insertar ---> "))
			if lugar <= 0:
				print("\n  ERROR...No. de sitio incorrecto!!")
			elif lugar == 1:
				self.crea_ins_ini_LDC()
			elif lugar > self.existenLDC:
				print(f"\n  Sólo existen {self.existenLDC} nodos...Se insertará al final")
				self.crea_ins_fin_LDC()
			else:
				self.crea_nodo_LD() #creacion del nodo
				self.nuevo.info = input("\n   Dato a insertar ---> ")
				
				if lugar == self.existenLDC:
					T = self.F.ant
					self.F.ant = self.nuevo
				else:
					Q = self.P.sig
					sitio = 1
					while lugar != sitio:
						Q = Q.sig
						sitio += 1
					T = Q.ant
					Q.ant = self.nuevo
				
				T.sig = self.nuevo
				self.nuevo.ant = T
				self.existenLDC += 1
	
	#------------------------- ELIMINAR POR INFO -------------------------#
	def eliminaInfo_LDC(self):
		if self.P.sig != self.P:
			X = input("\n    Ingrese el valor del nodo a eliminar ---> ")
			if self.F.info == X:
				if self.P.sig == self.F:
					self.P.sig = self.P
					self.P.ant = self.P
					self.F = None
				else:
					Q = self.F
					self.F = self.F.ant
					self.F.sig = self.P
					self.P.ant = self.F
					Q = None
					
				self.existenLDC -= 1
				print(f"\n  ¡¡El dato {X} fue eliminado!!\n")
				
			elif self.P.sig == self.F:
				print(f"\n  ¡¡No existe el dato {X}!!\n")
			else:
				Q = self.P.sig
				while(Q != self.P)and(Q.info != X):
				#while(Q.info != X)and(Q != None):
					Q = Q.sig
				if Q == self.P:
					print(f"\n   ¡¡No existe el dato {X}!!\n")
				else:
					if self.P.sig == Q:
						self.P.sig = Q.sig
					else:
						T = Q.ant
						T.sig = Q.sig
						if Q.sig == self.F:
							self.F.ant = Q.ant
						else:
							R = Q.sig
							R.ant = Q.ant
					Q = None
					self.existenLDC -= 1
					print(f"\n  ¡¡El dato {X} fue eliminado!!\n")
		else:
			print("\n\n null <- P -> null    ¡¡Lista Vacía!!\n\n")
	
	#------------------------- ELIMINAR POR No. NODO -------------------------#
	def eliminarNoNodo_LDC(self):
		if self.P.sig != self.P:
			lugar = int(input("\n   ¿Cuál es el número del nodo a eliminar? ---> "))
			if lugar <= 0:
				print("\n   ¡¡ERROR!!!...No. de nodo incorrecto!!!\n")
			elif lugar > self.existenLDC:
				print("\n   ¡¡No. de nodo superior a los que existen!!\n")
			elif lugar == self.existenLDC:
				print(f"\n   ¡¡El nodo no. {lugar} que contiene el dato: {self.F.info} fue eliminado!!\n")
				if self.P.sig == self.F:
					self.P.sig = self.P
					self.P.ant = self.P
					self.F = None
				else:
					Q = self.F
					self.F = self.F.ant
					self.F.sig = self.P
					self.P.ant = self.F
					Q = None
				self.existenLDC -= 1
			else:
				Q = self.P.sig
				sitio = 1
				while sitio != lugar:
					Q = Q.sig
					sitio += 1
				if self.P.sig == Q:
					self.P.sig = Q.sig
				else:
					T = Q.ant
					T.sig = Q.sig
					if Q.sig == self.F:
						self.F.ant = Q.ant
				print(f"\n   ¡¡El nodo no. {lugar} que contiene el dato: {Q.info} fue eliminado!!\n")
				Q = None
				self.existenLDC -= 1
		else:
			print("\n\n  null <- P -> null    ¡¡Lista Vacía!!\n\n")










