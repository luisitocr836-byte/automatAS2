from Libreria.Pila.pila import Pila
from Libreria.edNoLineales.ArbolBB import ArbolBB


class Arbol_expresiones(object):
    """Clase para construir y recorrer un árbol de expresiones usando
    la pila definida en `pila.py` y los nodos/recorridos de `ArbolBB`.
    """
    OPERADORES = set(['+', '-', '*', '/', '^'])

    def __init__(self):
        self.pila = Pila()
        self.root = None

    def construir_desde_postfija(self, expresion_postfija):
        """Construye el árbol a partir de una expresión en notación postfija.
        Los tokens deben estar separados por espacios.
        """
        self.pila.reiniciar()
        tokens = expresion_postfija.split()
        for t in tokens:
            if t in self.OPERADORES:
                # operador: pop derecha e izquierda, crear nodo y apilar
                if self.pila.pila_vacia():
                    raise ValueError("Expresión inválida: faltan operandos")
                right = self.pila.eliminar()
                if self.pila.pila_vacia():
                    raise ValueError("Expresión inválida: faltan operandos")
                left = self.pila.eliminar()
                nodo = ArbolBB(t, left, right)
                self.pila.insertar(nodo)
            else:
                # operando: crear nodo hoja y apilar
                nodo = ArbolBB(t, None, None)
                self.pila.insertar(nodo)

        if self.pila.pila_vacia():
            raise ValueError("Expresión vacía o inválida")
        self.root = self.pila.eliminar()
        if not self.pila.pila_vacia():
            raise ValueError("Expresión inválida: quedan elementos en la pila")

    def _recorrido_usando_ArbolBB(self, tipo):
        """Utiliza los métodos de `ArbolBB` para generar el recorrido como cadena.
        `tipo` debe ser 'preorden', 'inorden' o 'postorden'.
        """
        if self.root is None:
            return ""
        helper = ArbolBB(None, None, None)
        helper.listABB = ""
        if tipo == 'preorden':
            helper.preorden(self.root)
        elif tipo == 'inorden':
            helper.inorden(self.root)
        elif tipo == 'postorden':
            helper.postorden(self.root)
        else:
            raise ValueError("Tipo de recorrido desconocido")
        return helper.listABB.strip()

    def recorrido_preorden(self):
        return self._recorrido_usando_ArbolBB('preorden')

    def recorrido_inorden(self):
        return self._recorrido_usando_ArbolBB('inorden')

    def recorrido_postorden(self):
        return self._recorrido_usando_ArbolBB('postorden')

    def _tokenize(self, expresion):
        tokens = []
        i = 0
        while i < len(expresion):
            c = expresion[i]
            if c.isspace():
                i += 1
                continue
            if c.isalnum() or c == '.':
                j = i
                while j < len(expresion) and (expresion[j].isalnum() or expresion[j] == '.'):
                    j += 1
                tokens.append(expresion[i:j])
                i = j
                continue
            if c in ('+', '-', '*', '/', '^', '(', ')'):
                tokens.append(c)
                i += 1
                continue
            # cualquier otro carácter se toma como token separado
            tokens.append(c)
            i += 1
        return tokens

    def _infix_to_postfix(self, tokens):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        output = []
        stack = []
        for token in tokens:
            if token.isalnum() or ('.' in token) or (token and token[0].isalpha()):
                output.append(token)
            elif token in precedence:
                while stack and stack[-1] != '(' and (
                    (precedence.get(stack[-1], 0) > precedence[token]) or
                    (precedence.get(stack[-1], 0) == precedence[token] and token != '^')
                ):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack or stack[-1] != '(':
                    raise ValueError('Paréntesis desbalanceados')
                stack.pop()
            else:
                # tokens desconocidos se añaden directamente
                output.append(token)

        while stack:
            if stack[-1] in ('(', ')'):
                raise ValueError('Paréntesis desbalanceados')
            output.append(stack.pop())
        return output

    def construir_desde_infija(self, expresion_infija):
        """Convierte una expresión infija (puede contener paréntesis) a postfija
        y construye el árbol de expresiones.
        """
        tokens = self._tokenize(expresion_infija)
        postfix_tokens = self._infix_to_postfix(tokens)
        postfix = ' '.join(postfix_tokens)
        self.construir_desde_postfija(postfix)
