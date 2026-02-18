from pila import Pila

mi_pila = Pila()
if mi_pila.pila_vacia():
    print("La pila está vacía")  # salida: La pila está vacía
mi_pila.insertar("A")
mi_pila.insertar("r")
mi_pila.insertar("B")
print("el contenido de la pila es:\n", mi_pila.imprime())
                 
