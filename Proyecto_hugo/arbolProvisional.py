# interfaz_arbol_expresiones.py
# GUI que ofrece:
# - Modo BST: acepta enteros y letras (ordena lexicográficamente si son letras)
# - Modo Expresión: parsea expresiones infijas (ej. 4-5/(7+8)^9) y construye el árbol de expresión
# - Dibuja el árbol en pantalla
import tkinter as tk
from tkinter import ttk, messagebox
from Libreria.edNoLineales.ArbolBB import ArbolBB

# Nodo compatible con ArbolBB (usa atributos info, izq, der)
class ExprNode:
    def __init__(self, info, izq=None, der=None):
        self.info = info
        self.izq = izq
        self.der = der

class TreeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Árbol: BST y Expresiones")
        self.geometry("1000x650")
        # usamos self.nodo_raiz como la raíz actual; puede ser un nodo ArbolBB o ExprNode
        self.nodo_raiz = None
        self._build_ui()
        self.x_gap = 70
        self.y_gap = 100
        self.node_radius = 20

    def _build_ui(self):
        top = ttk.Frame(self)
        top.pack(side="top", fill="x", padx=6, pady=6)
        ttk.Label(top, text="Entrada:").pack(side="left")
        self.entry = ttk.Entry(top, width=30)
        self.entry.pack(side="left", padx=4)
        ttk.Button(top, text="Insertar (BST)", command=self.insertar_bst).pack(side="left", padx=3)
        ttk.Button(top, text="Usar Expresión", command=self.usar_expresion).pack(side="left", padx=3)
        ttk.Button(top, text="Limpiar", command=self.limpiar).pack(side="left", padx=3)
        ttk.Button(top, text="Redibujar", command=self.redibujar).pack(side="left", padx=3)
        ttk.Button(top, text="Mostrar Inorden", command=self.mostrar_inorden).pack(side="left", padx=3)
        # Recorridos: selector y botón
        self.opcion_recorrido = ttk.Combobox(top, values=["Inorden", "Preorden", "Postorden"], state="readonly", width=12)
        self.opcion_recorrido.current(0)
        self.opcion_recorrido.pack(side="left", padx=6)
        self.btn_recorrer = ttk.Button(top, text="Recorrer", command=self.iniciar_recorrido)
        self.btn_recorrer.pack(side="left", padx=3)
        # Resultado del recorrido (parte superior derecha)
        self.etiqueta_recorrido = ttk.Label(top, text="Recorrido:")
        self.etiqueta_recorrido.pack(side="right", padx=(4,0))
        self.resultado_recorrido = ttk.Label(top, text="", width=36, anchor="e")
        self.resultado_recorrido.pack(side="right", padx=4)

        # Cuadro grande para mostrar el recorrido (parte superior del área del árbol)
        self.recorrido_grande = tk.Text(self, height=4, wrap='word', font=("Segoe UI", 14), bg="#f7f7f7")
        self.recorrido_grande.insert('1.0', '')
        self.recorrido_grande.config(state='disabled')
        self.recorrido_grande.pack(fill="x", padx=6, pady=(0,6))

        # Canvas para dibujar el árbol (queda debajo del cuadro de recorrido)
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True, padx=6, pady=(0,6))
        self.status = ttk.Label(self, text="", anchor="w")
        self.status.pack(side="bottom", fill="x")

    # ---------------- BST insertion (accepts numbers and letters) ----------------
    def insertar_bst(self):
        """Inserta un valor usando la lógica de ArbolBB sin modificar su archivo.

        Aprovechamos el método `insertar` de la clase que solicita entrada mediante
        `input()`. Para evitar interacción por consola reemplazamos temporalmente
        la función builtin `input` por una que devuelve el texto de la caja.
        Después actualizamos `self.nodo_raiz` con la raíz resultante del contenedor
        `arb.P.izq`.
        """
        entrada = self.entry.get().strip()
        if entrada == "":
            messagebox.showwarning("Entrada", "Escribe un valor (número o letra).")
            return
        # creamos un contenedor ArbolBB que mantiene la cabecera en P
        arb = ArbolBB(None, None, None)
        arb.crea_cab()
        arb.P.izq = self.nodo_raiz
        # decidimos el tipo de conversión a pasar (int o str)
        tipo = int
        try:
            tipo(entrada)
        except Exception:
            tipo = str
        # parcheamos input para que devuelva la entrada deseada
        old_input = __builtins__['input']
        try:
            __builtins__['input'] = lambda prompt='': entrada
            arb.insertar(tipo)
        finally:
            __builtins__['input'] = old_input
        # extraemos árbol actualizado
        self.nodo_raiz = arb.P.izq
        self.entry.delete(0, 'end')
        self.redibujar()

    # ---------------- Expression parsing & tree ----------------
    def usar_expresion(self):
        expresion = self.entry.get().strip()
        if expresion == "":
            messagebox.showwarning("Entrada", "Escribe una expresión como 4-5/(7+8)^9 o letras.")
            return
        try:
            postfija = self._infija_a_postfija(expresion)
            raiz = self._postfija_a_arbol(postfija)
            self.nodo_raiz = raiz
            self.entry.delete(0, 'end')
            self.redibujar()
        except Exception as e:
            messagebox.showerror("Parseo", f"Error parseando la expresión: {e}")

    def _infija_a_postfija(self, cadena):
        # Tokenizar: números, identificadores (letras), operadores, paréntesis
        tokens = []
        i=0
        while i < len(cadena):
            c = cadena[i]
            if c.isspace():
                i+=1; continue
            if c.isdigit():
                num = c
                i+=1
                while i < len(cadena) and cadena[i].isdigit():
                    num += cadena[i]; i+=1
                tokens.append(num)
                continue
            if c.isalpha():
                ident = c
                i+=1
                while i < len(cadena) and cadena[i].isalnum():
                    ident += cadena[i]; i+=1
                tokens.append(ident)
                continue
            if c in "+-*/^()":
                tokens.append(c); i+=1; continue
            raise ValueError(f"Caracter inválido: {c}")
        # shunting-yard
        prec = {'^':4, '*':3, '/':3, '+':2, '-':2}
        asoci_derecha = {'^'}
        salida=[]
        pila=[]
        for t in tokens:
            if t.isalnum():
                salida.append(t)
            elif t in prec:
                while pila and pila[-1] in prec:
                    top = pila[-1]
                    if (prec[top] > prec[t]) or (prec[top]==prec[t] and t not in asoci_derecha):
                        salida.append(pila.pop()); continue
                    break
                pila.append(t)
            elif t == '(':
                pila.append(t)
            elif t == ')':
                while pila and pila[-1] != '(':
                    salida.append(pila.pop())
                if not pila or pila[-1] != '(':
                    raise ValueError("Paréntesis desbalanceados")
                pila.pop()
        while pila:
            if pila[-1] in '()':
                raise ValueError("Paréntesis desbalanceados")
            salida.append(pila.pop())
        return salida

    def _postfija_a_arbol(self, postfija):
        pila=[]
        ops = set(['+','-','*','/','^'])
        for tok in postfija:
            if tok in ops:
                if len(pila) < 2:
                    raise ValueError("Expresión inválida")
                derecho = pila.pop()
                izquierdo = pila.pop()
                nodo = ExprNode(tok, izquierdo, derecho)
                pila.append(nodo)
            else:
                try:
                    valor = int(tok)
                except:
                    valor = tok
                pila.append(ExprNode(valor))
        if len(pila) != 1:
            raise ValueError("Expresión inválida")
        return pila[0]

    # ---------------- Drawing ----------------
    def redibujar(self):
        self.canvas.delete("all")
        self.node_items = {}
        if self.nodo_raiz is None:
            self.status.config(text="Árbol vacío.")
            return
        self.positions = {}
        self.x_counter = 0
        self._asignar_coords(self.nodo_raiz, depth=0)
        width = max(800, (self.x_counter + 1) * self.x_gap + 60)
        height = max(300, (self._profundidad_maxima(self.nodo_raiz) + 2) * self.y_gap + 60)
        self.canvas.config(scrollregion=(0,0,width,height))
        self._dibujar_aristas(self.nodo_raiz)
        self._dibujar_nodos()
        self.status.config(text=f"Nodos: {self.x_counter}")

    def _asignar_coords(self, nodo, depth):
        if nodo is None:
            return
        self._asignar_coords(nodo.izq, depth+1)
        x = self.x_counter * self.x_gap + 60
        y = depth * self.y_gap + 60
        self.positions[nodo] = (x,y)
        self.x_counter += 1
        self._asignar_coords(nodo.der, depth+1)

    def _profundidad_maxima(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._profundidad_maxima(nodo.izq), self._profundidad_maxima(nodo.der))

    def _dibujar_aristas(self, nodo):
        if nodo is None:
            return
        if nodo.izq:
            x1,y1 = self.positions[nodo]; x2,y2 = self.positions[nodo.izq]
            self.canvas.create_line(x1, y1, x2, y2, width=2)
        if nodo.der:
            x1,y1 = self.positions[nodo]; x2,y2 = self.positions[nodo.der]
            self.canvas.create_line(x1, y1, x2, y2, width=2)
        self._dibujar_aristas(nodo.izq)
        self._dibujar_aristas(nodo.der)

    def _dibujar_nodos(self):
        for nodo, (x,y) in self.positions.items():
            r = self.node_radius
            oval = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="#ffd97d", outline="#333")
            text = self.canvas.create_text(x, y, text=str(nodo.info), font=("Segoe UI", 10, "bold"))
            self.node_items[nodo] = (oval, text)

    def mostrar_inorden(self):
        """Muestra el recorrido inorden usando el método de ArbolBB."""
        if self.nodo_raiz is None:
            messagebox.showinfo("Inorden", "Árbol vacío.")
            return
        arb = ArbolBB(None, None, None)
        # reutilizamos inorden de ArbolBB para formar la cadena
        arb.listABB = ""
        arb.inorden(self.nodo_raiz)
        messagebox.showinfo("Inorden", arb.listABB.strip())

    # ---------------- Recorridos animados ----------------
    def _colectar_inorden(self, nodo, lista):
        if nodo is None: return
        self._colectar_inorden(nodo.izq, lista)
        lista.append(nodo)
        self._colectar_inorden(nodo.der, lista)

    def _colectar_preorden(self, nodo, lista):
        if nodo is None: return
        lista.append(nodo)
        self._colectar_preorden(nodo.izq, lista)
        self._colectar_preorden(nodo.der, lista)

    def _colectar_postorden(self, nodo, lista):
        if nodo is None: return
        self._colectar_postorden(nodo.izq, lista)
        self._colectar_postorden(nodo.der, lista)
        lista.append(nodo)

    def iniciar_recorrido(self):
        if self.nodo_raiz is None:
            messagebox.showinfo("Recorrido", "Árbol vacío.")
            return
        if getattr(self, 'recorrido_ejecutandose', False):
            return
        opcion = self.opcion_recorrido.get()
        # recolectar nodos manualmente copiar método de ArbolBB pero en esta clase
        nodos = []
        if opcion == "Inorden":
            self._colectar_inorden(self.nodo_raiz, nodos)
        elif opcion == "Preorden":
            self._colectar_preorden(self.nodo_raiz, nodos)
        else:
            self._colectar_postorden(self.nodo_raiz, nodos)
        self.recorrido_ejecutandose = True
        self.btn_recorrer.state(['disabled'])
        self.resultado_recorrido.config(text="")
        self.recorrido_grande.config(state='normal')
        self.recorrido_grande.delete('1.0', 'end')
        self.recorrido_grande.tag_configure('center', justify='center')
        self._animar_recorrido(nodos, 0, [])

    def _animar_recorrido(self, nodos, idx, acumulado):
        if idx > 0:
            anterior = nodos[idx-1]
            if anterior in self.node_items:
                oval, _ = self.node_items[anterior]
                self.canvas.itemconfig(oval, fill="#ffd97d")
        if idx >= len(nodos):
            self.recorrido_ejecutandose = False
            self.btn_recorrer.state(['!disabled'])
            self.recorrido_grande.config(state='disabled')
            return
        nodo = nodos[idx]
        if nodo in self.node_items:
            oval, _ = self.node_items[nodo]
            self.canvas.itemconfig(oval, fill="#ff6b6b")
        acumulado.append(str(nodo.info))
        texto = " ".join(acumulado)
        self.resultado_recorrido.config(text=texto)
        self.recorrido_grande.config(state='normal')
        self.recorrido_grande.delete('1.0', 'end')
        self.recorrido_grande.insert('1.0', texto, 'center')
        self.recorrido_grande.config(state='disabled')
        self.after(650, lambda: self._animar_recorrido(nodos, idx+1, acumulado))

    def limpiar(self):
        self.nodo_raiz = None
        self.canvas.delete("all")
        self.status.config(text="Árbol limpiado.")

if __name__ == "__main__":
    app = TreeApp()
    app.mainloop()