#TECNOLOGICO NACIONAL DE MEXICO CAMPUS SAN JUAN DEL RIO
#Ing. en Sistemas Computacionales
#Estructura de datos
#Tema III. Recursividad, arboles y grafos
#Practica 4. Arboles Binarios
#Hugo Francisco Martinez Briseño

from Libreria.edNoLineales.ArbolBB import ArbolBB
#deja que los perros ladren huachimingo es señal de que avanzamos
#saca el pornooooooooooooooooooooooooooo


#--------------------- MENU ---------------------#
def menu(op):
	while op < 1 or op > 7:
		print("\n\n     *** MENÚ ÁRBOL BINARIO DE BÚSQUEDA ***") 
		print("\n         1. Crear / Insertar nodo") 
		print("         2. Recorrido Preorden") 
		print("         3. Recorrido Inorden") 
		print("         4. Recorrido Postorden") 
		print("         5. Eliminación") 
		print("         6. Buscar") 
		print("         7. Salir")
		op = int(input("\n      Elige una opción -> "))
		if op < 1 or op > 7: 
			print("\n\n      ¡¡¡ERROR!!!, la opción debe ser del 1 al 7\n") 
   
	return op 

#--------------------- MAIN ---------------------#

objABB = ArbolBB(None,None,None)
objABB.crea_cab()

r = 0
while r != 7:
	r = menu(0)
	if r != 7:
		if r == 1:
			objABB.insertar(int)
		else:
			if objABB.P.izq == None:
				print("\n ¡¡Árbol vacío!! \n")
			else:
				if r == 2:
					objABB.listABB = "\n "
					objABB.preorden(objABB.P.izq)
					print("\n PREORDEN: ",objABB.listABB)
				elif r == 3:
					objABB.listABB = "\n "
					objABB.inorden(objABB.P.izq)
					print("\n INORDEN: ",objABB.listABB)
				elif r == 4:
					objABB.listABB = "\n "
					objABB.postorden(objABB.P.izq)
					print("\n POSTORDEN: ",objABB.listABB)
				elif r == 5:
					objABB.elimina1()
				elif r == 6:
					objABB.b = 0
					objABB.x = int(input("\n¿Cuál es el dato a buscar? -> "))
					objABB.buscar(objABB.P.izq)
					if (objABB.b == 0):
						print(f"\n El dato {objABB.x} NO existe en el ABB")
print("\n\n*** FIN DE LA APLICACIÓN ***\n")
