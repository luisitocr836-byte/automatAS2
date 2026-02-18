class nodoPila(object): #DECLARACION DE NODO QUE RECIBE UN OBJETO
    dato = None      # TIENE DOS SEGMENTOS: DATO Y SIGUIETE
    siguiente = None  #AMBOS AL PRNCIPIO SERAN DE TIPO NONE

class Pila(object): #DECLARACION DE LA PILA
    def __init__(self): # INICIALIZACION DE LA PILA
        self.cima = None #NUESTRA PILA INICIA VACIA, POR LO TANTO LA CIMA ES NONE

    def reiniciar(self): #METODO PARA REINICIAR LA PILA
        self.cima = None
    
    def insertar(self,dato):
        nodo =nodoPila() #CREACION DE UN NODO
        nodo.dato = dato
        nodo.siguiente = self.cima #EL SIGUIENTE DEL NODO APUNTA A LA CIMA ACTUAL 
        self.cima =nodo #LA CIMA AHORA ES EL NUEVO NODO

    def eliminar(self):
        x = self.cima.dato #SE GUARDA EL DATO DE LA CIMA
        nodo_eliminar = self.cima #SE GUARDA EL NODO A ELIMINAR
        self.cima = self.cima.siguiente #LA CIMA AHORA APUNTA AL SIGUIENTE
        nodo_eliminar.siguiente = None #EL NODO A ELIMINAR APUNTA A NONE
        return x #SE REGRESA EL DATO DE LA CIMA ELIMINADA
    
    def pila_vacia(self): #METODO PARA SABER SI LA PILA ESTA VACIA
        return self.cima is None  #REGRESA TRUE SI LA CIMA ES NONE, FALSE EN OTRO CASO
    
    def cima_pila(self): #METODO PARA OBTENER EL DATO DE LA CIMA
        if self.cima is not None: #SI LA CIMA NO ES NONE
            return self.cima.dato #REGRESA EL DATO DE LA CIMA
        else:
            return None #SI LA CIMA ES NONE, REGRESA NONE
        
    def imprime(self): #METODO PARA MOSTRAR LA PILA
        paux = Pila()
        cadena = ""
        while not self.pila_vacia(): #MIENTRAS LA PILA NO ESTE VACIA
            dato = self.eliminar() #SE ELIMINA EL DATO DE LA CIMA
            cadena += str(dato) + "\n" #SE AGREGA EL DATO A LA CADENA
            paux.insertar(dato) #SE INSERTA EL DATO EN LA PILA AUXILIAR
        
        while not paux.pila_vacia(): #MIENTRAS LA PILA AUXILIAR NO ESTE VACIA
            dato = paux.eliminar() #SE ELIMINA EL DATO DE LA CIMA DE LA PILA AUXILIAR
            self.insertar(dato) #SE INSERTA EL DATO EN LA PILA ORIGINAL
        return cadena #SE REGRESA LA CADENA CON LOS DATOS