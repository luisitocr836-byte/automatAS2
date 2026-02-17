# ---------------------------------------------------------
# ÁRBOL DE EXPRESIONES
# Convierte una expresión infija a postfija y construye
# su árbol binario de expresión
# ---------------------------------------------------------

# ------------------ CLASE NODO ------------------
class Nodo:
    def __init__(self, valor):
        self.valor = valor   # Guarda el carácter (operador u operando)
        self.izq = None      # Hijo izquierdo
        self.der = None      # Hijo derecho


# ------------------ PRIORIDAD DE OPERADORES ------------------
def prioridad(op):
    """
    Devuelve la prioridad del operador
    * y / tienen mayor prioridad que + y -
    """
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op in ('^'):
        return 3
    return 0


# ------------------ INFIJA → POSTFIJA ------------------
def infija_a_postfija(exp):
    """
    Convierte una expresión infija a postfija
    usando una pila (algoritmo tipo Shunting Yard)
    """
    pila = []     # Pila para operadores
    salida = []   # Lista donde se forma la expresión postfija

    for c in exp:
        
        if c.isalnum():  # Si es operando (letras o números)
            salida.append(c)

        elif c == '(':   # Si es paréntesis que abre
            pila.append(c)

        elif c == ')':   # Si es paréntesis que cierra
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # Elimina el '(' de la pila

        else:  # Si es operador (+, -, *, /)
            while pila and prioridad(c) <= prioridad(pila[-1]):
                salida.append(pila.pop())
            pila.append(c)

    # Vaciar la pila al final
    while pila:
        salida.append(pila.pop())

    return ''.join(salida)


# ------------------ CONSTRUIR ÁRBOL DESDE POSTFIJA ------------------
def construir_arbol(postfija):
    """
    Construye el árbol de expresión a partir de la expresión postfija
    """
    pila = []

    for c in postfija:
        nodo = Nodo(c)

        if c.isalnum():  # Si es operando, se apila directamente
            pila.append(nodo)
        else:
            # Si es operador, sacamos dos operandos de la pila
            nodo.der = pila.pop()  # El segundo operando es hijo derecho
            nodo.izq = pila.pop()  # El primero es hijo izquierdo
            pila.append(nodo)      # El nuevo subárbol se vuelve a apilar

    return pila.pop()  # La raíz del árbol


# ------------------ RECORRIDOS DEL ÁRBOL ------------------
def preorden(nodo):
    """Raíz - Izquierda - Derecha"""
    if nodo:
        print(nodo.valor, end=' ')
        preorden(nodo.izq)
        preorden(nodo.der)


def inorden(nodo):
    """Izquierda - Raíz - Derecha"""
    if nodo:
        inorden(nodo.izq)
        print(nodo.valor, end=' ')
        inorden(nodo.der)


def postorden(nodo):
    """Izquierda - Derecha - Raíz"""
    if nodo:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(nodo.valor, end=' ')


# ------------------ PROGRAMA PRINCIPAL ------------------


print("\n*** ÁRBOL DE EXPRESIONES ***")

expresion = input("\nIngresa la expresión infija: ")

# Convertir a postfija
postfija = infija_a_postfija(expresion)
print("\nExpresión en postfija:", postfija)

# Construir árbol
raiz = construir_arbol(postfija)

# Mostrar recorridos
print("\nRecorrido Preorden:")
preorden(raiz)

print("\n\nRecorrido Inorden:")
inorden(raiz)

print("\n\nRecorrido Postorden:")
postorden(raiz)

print("\n")

