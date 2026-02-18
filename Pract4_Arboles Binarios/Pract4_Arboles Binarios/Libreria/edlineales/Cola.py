#TECNOLÓGICO NACIONAL DE MÉXICO CAMPUS SAN JUAN DEL RÍO 
#Ingeniería en Sistemas Computacionales
#CLASE GENERICA PARA LA GESTION DE COLAS
#Autor: Hugo Francisco Martinez Briseño
#Versión 1.0

class Cola:
#--------------------- CONSTRUCTOR ----------------------#
	def __init__(self, frente,final):
		self.frente = frente
		self.final = final


#            * * * C O L A    S I M P L E * * *
#--------------------- INSERTAR ----------------------#
	def insertar_cs(self,cola,MAX):
		if self.final < MAX-1:
			self.final += 1
			cola[self.final] = input("   Ingrese el valor a insertar -> ")
			print("\n   ¡",cola[self.final]," a sido insertado! \n")
			
			if self.final == 0:
				self.frente = 0 
			
		else:
			print("\n\n  ¡COLA LLENA!")#Overflow

#--------------------- ELIMINAR ----------------------#
	def eliminar_cs(self,cola,ban):
		if self.frente != -1:
			print("\n  ¡", cola[self.frente]," hasido eliminado!\n\n")
			if ban:
				cola[self.frente] = "" #Omitir para eliminacion logica
			if self.frente == self.final:
				self.frente = self.final = -1
			else:
				self.frente += 1
		else:
			print("\n\n  ¡COLA VACIA!")#Underflow


#	* *  C O L A  C I R C U L A R  * *

# ----------- INSERTAR ----------- #
	def insertar_cc(self,colacirc,MAX):
		if (self.final == MAX-1 and self.frente == 0) or (self.final + 1 == self.frente):
			print("\n\n	¡COLA LLENA! \n\n") #Overflow
		else:
			if self.final == MAX -1:
				self.final = 0
			else:
				self.final +=  1
			colacirc[self.final] = input("\n	Ingrese el valor a insertar: ")
			if self.frente == -1:
				self.frente = 0
			print("\n ¡",colacirc[self.final]," ha sido insertado! \n")

# ----------- ELIMINACIÓN ----------- #
	def eliminar_cc(self,colacirc,MAX,ban):
		
		if self.frente == -1:
			print("\n\n	¡COLA VACÍA! \n\n") #Underflow
		else:
			print("\n ¡",colacirc[self.frente]," ha sido eliminado! \n")
			if ban:
				colacirc[self.frente] = " "
			if self.frente == self.final:
				self.frente = self.final = -1
			elif self.frente == MAX-1:
				self.frente = 0
			else:
				self.frente += 1

#	* *  C O L A  D O B L E  * *

# ----------- INSERTAR ----------- #
	def insertar_bc(self,bicola,MAX,op):
		if self.final < MAX-1 or self.frente > 0:
			if self.frente == -1 and self.final == -1:
				self.frente = MAX // 2
				self.final = MAX // 2
				bicola[self.frente] = input("\n	Ingrese el valor a insertar: ")
			else:
				if op == 1: #Inserción por el frente
					if self.frente != 0:
						self.frente -= 1
						bicola[self.frente] = input("\n	Ingrese el valor a insertar: ")
						print(f"\n¡{bicola[self.frente]} ha sido insertado!\n")
					else:
						print("\n¡BICOLA LLENA POR EL FRENTE!\n")
				else: #Inserción por el final
					if self.final == MAX-1:
						print("\n¡BICOLA LLENA POR EL FINAL!\n")
					else:
						self.final += 1
						bicola[self.final] = input("\n	Ingrese el valor a insertar: ")
						print(f"\n¡{bicola[self.final]} ha sido insertado!\n")
		else:
			print("\n\n	¡BICOLA LLENA! \n\n")

# ----------- ELIMINACIÓN ----------- #
	def eliminar_bc(self, bicola, MAX, opER, ban):
			if self.frente == -1:
				print("\n¡BICOLA VACÍA!\n")
			else:
				if opER == 1:  # Eliminación por el frente
					print(f"\n¡{bicola[self.frente]} ha sido eliminado del frente!\n")
					if ban:
						bicola[self.frente] = " "
					if self.frente == self.final:
						self.frente = self.final = -1
					elif self.frente == MAX - 1:
						self.frente = 0
					else:
						self.frente += 1
				else:  # Eliminación por el final
					print(f"\n¡{bicola[self.final]} ha sido eliminado del final!\n")
					if ban:
						bicola[self.final] = " "
					if self.frente == self.final:
						self.frente = self.final = -1
					else:
						self.final -= 1

#	* *  C O L A  D E  P R I O R I D A D * *

# ----------- INSERTAR ----------- #
	def insertar_cp(self, CP, MAX):
		if self.final == MAX - 1:
			print("\nCola de Prioridades llena")
		else:
			dat = input("\nIngrese el valor a insertar: ")
			pr = int(input("\nIngrese la prioridad: "))

			if self.frente == -1 and self.final == -1:  # Primer elemento
				self.frente = 0
				self.final = 0
				CP[self.final][0] = pr
				CP[self.final][1] = dat
			else:
				self.final += 1  # Se incrementa el final ya que habrá un nuevo elemento

				# Si el nuevo dato tiene mayor o igual prioridad que el último, se inserta al final
				if CP[self.final - 1][0] <= pr:
					CP[self.final][0] = pr
					CP[self.final][1] = dat
				else:
					# Desplazar hacia la derecha los elementos de mayor prioridad para hacer espacio
					for x in range(self.frente, self.final):
						if CP[x][0] > pr:
							# Desplazar elementos para insertar el nuevo en su lugar correcto
							for y in range(self.final, x, -1):
								CP[y][0] = CP[y - 1][0]
								CP[y][1] = CP[y - 1][1]
							# Inserción del nuevo elemento
							CP[x][0] = pr
							CP[x][1] = dat
							break

# ----------- ELIMINACIÓN ----------- #
	def eliminar_cp(self, CP, MAX):
		if self.frente == -1:
			print("\n¡Cola de Prioridades vacía!\n")
		else:
			print(f"\n¡El dato {CP[self.frente][1]} ha sido eliminado!\n")

			if self.frente == self.final:
				CP[self.frente][0] = " "
				CP[self.frente][1] = " "
				self.frente = -1
				self.final = -1
			else:
				for i in range(self.frente, self.final):
					CP[i][0] = CP[i + 1][0]
					CP[i][1] = CP[i + 1][1]

				CP[self.final][0] = " "
				CP[self.final][1] = " "
				self.final -= 1
				self.frente = 0
