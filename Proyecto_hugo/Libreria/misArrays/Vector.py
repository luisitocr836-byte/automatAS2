#TECNOLÓGICO NACIONAL DE MÉXICO CAMPUS SAN JUAN DEL RÍO 
#Ingeniería en Sistemas Computacionales
#Autor: Hugo Francisco Martinez Briseño
#Versión 1.0

class Vector:

#----------------- VARIABLE ---------------#
	i = 0

#---------------- LEER / ENTRADA ----------#
#Sin genericidad
#De 0 a N-1
	def leer_vec(self,vec,N):
		for i in range(N):
			vec[i] = input("\n  Vector["+str(i+1)+"] = ")

#De N-1 a 0
	def leer_vec_inv(self,vec,N):
		for i in range(N-1,-1,-1):
			vec[i] = input("\n  Vector["+str(i+1)+"] = ")

#Con genericidad
#De 0 a N-1
	def leer_vec_etiq(self,vec,N,etiq):
		for i in range(N):
			vec[i] = input("\n  "+etiq+" "+str(i+1)+": ")

#De N-1 a 0
	def leer_vec_inv_etiq(self,vec,N,etiq):
		for i in range(N-1,-1,-1):
			vec[i] = input("\n  "+etiq+" "+str(i+1)+": ")

#---------------- IMPRIMIR / SALIDA -------#
#Sin genericidad
#De 0 a N-1
	def imprimir_vec(self,vec,N):
		for i in range(N):
			print("\n  Vector["+str(i+1)+"] = ",vec[i])

#De N-1 a 0
	def imprimir_vec_inv(self,vec,N):
		for i in range(N-1,-1,-1):
			print("\n  Vector["+str(i+1)+"] = ",vec[i])

#Con genericidad
#De 0 a N-1
	"""
	def imprimir_vec_etiq(self,vec,N,etiq):
		for i in range(N):
			print("\n  "+etiq+" "+str(i+1)+": ",vec[i])
	"""
	def imprimir_vec_etiq(self,vec, N, etiq):
		for i in range(N):
			if vec[i] != "":
				print("\n  " + etiq + " " + str(i + 1) + ": ", vec[i])

#De N-1 a 0
	def imprimir_vec_inv_etiq(self,vec,N,etiq):
		for i in range(N-1,-1,-1):
			print("\n  "+etiq+" "+str(i+1)+": ",vec[i])
	
	def imprimir_vec_LimI_LimS(self,vec,LimInf,LimSup,etiq):
		for i in range(LimInf,LimSup+1,1):
			print("\n "+etiq+" "+str(i+1)+": ",vec[i])
	
	def imprimir_vec_limInfSup_LimSup(self,vec,infe,sup,etiq):
		for i in range(sup,infe-1,-1):
			print("\n "+etiq+" "+str(i+1)+": ",vec[i])
			 
	def imprimir_circular_vec(self,vec,N,infe,sup,etiq):
		for i in range(infe,N):
			print("      "+etiq+"["+str(i + 1)+"] = "+str(vec[i]))
			if i == N-1:
				for j in range(0,sup+1):
					print("      "+etiq+"["+str(j + 1)+"] = "+str(vec[j]))
	
	













