#TECNOLÓGICO NACIONAL DE MÉXICO CAMPUS SAN JUAN DEL RÍO 
#Ingeniería en Sistemas Computacionales
#CLASE GEBERICA PARA LA GESTION DE MATRICES
#Autor:Hugo Francisco Martinez Briseño
#Versión 1.0

class Matriz:
	#--------------------- VARIABLES MIEMBRO ---------------------#
	f = c = 0
	
	#----------------------- LEER / ENTRADA ----------------------#
	#Sin Genericidad
	#Por filas
	def leer_mat_fil(self,mat,M,N):
		for f in range(M):
			for c in range(N):
				mat[f][c] = input("\n	Matriz["+str(f+1)+"]["+str(c+1)+"] = ")
	
	#Por columnas
	def leer_mat_col(self,mat,M,N):
		for c in range(N):
			for f in range(M):
				mat[f][c] = input("\n	Matriz["+str(f+1)+"]["+str(c+1)+"] = ")
	
	#Con Genericidad
	#Por filas
	def leer_mat_fil_etiq(self,mat,M,N,etiq):
		for f in range(M):
			for c in range(N):
				mat[f][c] = input("\n	"+etiq+" "+str(f+1)+","+str(c+1)+": ")
	
	#Por columnas
	def leer_mat_col_etiq(self,mat,M,N,etiq):
		for c in range(N):
			for f in range(M):
				mat[f][c] = input("\n	"+etiq+" "+str(f+1)+","+str(c+1)+": ")
	
	#PARALELA CON VECTORES DE LETREROS
	def leer_mat_let(self,mat,M,N,let,let2):
		for f in range(M):
			print("\n"+let[0]+": "+let2[f])
			mat[f][0] = let2[f]
			for c in range(1,N):
				#mat[f][c] = int(input("\n	"+let[c]+": "))
				mat[f][c] =  int(input("\n	"+let[c]+": "))
	
	#--------------------- IMPRIMIR / SALIDA ---------------------#
	#Sin Generosidad
	#Por filas
	def imprimir_mat_fil(self,mat,M,N):
		for f in range(M):
			for c in range(N):
				print("\n	Matriz["+str(f+1)+"]["+str(c+1)+"] = ",mat[f][c])
	
	#Por columnas
	def imprimir_mat_col(self,mat,M,N):
		for c in range(N):
			for f in range(M):
				print("\n	Matriz["+str(f+1)+"]["+str(c+1)+"] = ",mat[f][c])
	
	#Con Generosidad
	#Por filas
	def imprimir_mat_fil_etiq(self,mat,M,N,etiq):
		for f in range(M):
			for c in range(N):
				print("\n	"+etiq+" "+str(f+1)+","+str(c+1)+": ",mat[f][c])
	
	#Por columnas
	def imprimir_mat_col_etiq(self,mat,M,N,etiq):
		for c in range(N):
			for f in range(M):
				print("\n	"+etiq+" "+str(f+1)+","+str(c+1)+": ",mat[f][c])

	#SIN ETIQUETAS
	def imprimir_mat_sinEtiq(self, M, N, mat,etiq1,etiq2):
		print(f"\n{etiq1}  *  {etiq2}   *")
		for f in range(M):
			linea = "    "
			for c in range(N):
				if mat[f][c] == " " or mat[f][c] is None:
					linea += "0    "
				else:
					linea += str(mat[f][c]) + "    *    "
			print("\n" + linea)
	
	def imprimir_mat_etiq2(self, M, N, mat,etiq1,etiq2):
		print(f"\n{etiq1}  *  {etiq2}   *")
		for f in range(M):
			linea = "      "
			for c in range(N):
				linea += str(mat[f][c]) + "    *    "
			print("\n" + linea)
			#linea = "	"
