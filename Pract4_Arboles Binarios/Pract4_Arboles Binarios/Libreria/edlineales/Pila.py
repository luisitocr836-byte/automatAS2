#TECNOLÓGICO NACIONAL DE MÉXICO CAMPUS SAN JUAN DEL RÍO 
#Ingeniería en Sistemas Computacionales
#CLASE GENERICA PARA LA GESTION DE PILAS
#Autor: Hugo Francisco Martinez Briseño
#Versión 1.0

class Pila:
	
	#--------------- CONSTRUCTOR ------------------#
	def __init__(self,tope):
		self.tope = tope
	#--------------- PUSH / INSERTAR --------------#
	def push(self,pila,MAX):
		if self.tope < MAX -1:
			self.tope += 1
			pila[self.tope] = input("\n Ingrese el valor a insertar -> ")
			print(f"\n ¡{pila[self.tope]} ha sido insertado!\n\n")
		else:
			print("\n\n ¡¡PILA LLENA!!\n\n") #Overflow
	
	#-------------- POP / ELIMINAR -----------------#
	def pop(self,pila,ban):
		if self.tope > -1:
			print(f"\n ¡{pila[self.tope]} ha sido eliminado!\n\n")
			if ban:
				pila[self.tope] = ""
			self.tope -= 1
		else:
			print("\n\n ¡¡PILA VACIA!!\n\n") #Underflow
"""

#PRUEBA RAPIDA
#Practica 2

objPila = Pila(-1)
pila = [None] * 3

print("\n	*** PUSH ***\n")

for i in range(3):
	objPila.push(pila,3)
	
print("\n Los elementos de la pila son: \n")
print(pila)

print("\n	*** POP FISICO ***\n")
objPila.pop(pila,True)

print("\n Los elementos de la pila son: \n")
print(pila)

print("\n	*** POP LOGICO ***\n")
objPila.pop(pila,False)

print("\n Los elementos de la pila son: \n")
print(pila)

print("\n\n Fin de la prueba rapida...:)\n\n")
"""
