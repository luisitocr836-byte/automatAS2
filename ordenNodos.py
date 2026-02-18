#TECNOLOGICO NACIONAL DE MEXICO CAMPUS SAN JUAN DEL RIO
#Ing. en Sistemas Computacionales
#Luis eduardo cruz resendiz
#origiinal raiz

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
        
    def insertar(self,tipo):
        self.crea_nodo()
        self.nuevo.info = str(input("\n Ingrese el valor a insertar -> "))
        
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
            
            
            
#--------------------- MENU ---------------------#
def menu(op):
	while op < 1 or op > 5:
		print("\n\n     *** MENÚ ÁRBOL BINARIO DE BÚSQUEDA ***") 
		print("\n         1. Crear / Insertar nodo") 
		print("         2. Recorrido Preorden") 
		print("         3. Recorrido Inorden") 
		print("         4. Recorrido Postorden") 
		print("         5. Salir")
		op = int(input("\n      Elige una opción -> "))
		if op < 1 or op > 5: 
			print("\n\n      ¡¡¡ERROR!!!, la opción debe ser del 1 al 7\n") 
	return op 

#--------------------- MAIN ---------------------#
            
objABB = ArbolBB(None,None,None)
objABB.crea_cab()

r = 0
while r != 5:
	r = menu(0)
	if r != 5:
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
print("\n\n*** FIN DE LA APLICACIÓN ***\n")