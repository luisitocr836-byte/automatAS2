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
        # usamos self.root_node como la raíz actual; puede ser un ArbolBB node o ExprNode
        self.root_node = None
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
        ttk.Button(top, text="Insertar (BST)", command=self.insert_bst).pack(side="left", padx=3)
        ttk.Button(top, text="Usar Expresión", command=self.use_expression).pack(side="left", padx=3)
        ttk.Button(top, text="Limpiar", command=self.clear).pack(side="left", padx=3)
        ttk.Button(top, text="Redibujar", command=self.redraw).pack(side="left", padx=3)
        ttk.Button(top, text="Mostrar Inorden", command=self.show_inorden).pack(side="left", padx=3)
        # Recorridos: selector y botón
        self.trav_choice = ttk.Combobox(top, values=["Inorden", "Preorden", "Postorden"], state="readonly", width=12)
        self.trav_choice.current(0)
        self.trav_choice.pack(side="left", padx=6)
        self.btn_traverse = ttk.Button(top, text="Recorrer", command=self.start_traversal)
        self.btn_traverse.pack(side="left", padx=3)
        # Resultado del recorrido (parte superior derecha)
        self.trav_display_label = ttk.Label(top, text="Recorrido:")
        self.trav_display_label.pack(side="right", padx=(4,0))
        self.trav_result = ttk.Label(top, text="", width=36, anchor="e")
        self.trav_result.pack(side="right", padx=4)

        # Cuadro grande para mostrar el recorrido (parte superior del área del árbol)
        self.trav_large = tk.Text(self, height=4, wrap='word', font=("Segoe UI", 14), bg="#f7f7f7")
        self.trav_large.insert('1.0', '')
        self.trav_large.config(state='disabled')
        self.trav_large.pack(fill="x", padx=6, pady=(0,6))

        # Canvas para dibujar el árbol (queda debajo del cuadro de recorrido)
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True, padx=6, pady=(0,6))
        self.status = ttk.Label(self, text="", anchor="w")
        self.status.pack(side="bottom", fill="x")

    # ---------------- BST insertion (accepts numbers and letters) ----------------
    def insert_bst(self):
        s = self.entry.get().strip()
        if s == "":
            messagebox.showwarning("Entrada", "Escribe un valor (número o letra).")
            return
        # build node as ArbolBB-compatible object
        try:
            val = int(s)
            node = ArbolBB(val, None, None)
        except ValueError:
            node = ArbolBB(s, None, None)
        if self.root_node is None:
            # create a dummy P-like header to reuse structure
            header = ArbolBB(None, None, None)
            header.izq = node
            self.root_node = header.izq
        else:
            # current root might be either ArbolBB or ExprNode; if ExprNode, replace with BST root
            if isinstance(self.root_node, ExprNode):
                # replace whole tree with BST single node
                self.root_node = node
            else:
                Q = self.root_node
                while True:
                    # compare numeric when both ints, else string compare
                    a = node.info
                    b = Q.info
                    try:
                        if isinstance(a, int) and isinstance(b, int):
                            cmp = a <= b
                        else:
                            cmp = str(a) <= str(b)
                    except Exception:
                        cmp = str(a) <= str(b)
                    if cmp:
                        if Q.izq is None:
                            Q.izq = node
                            break
                        Q = Q.izq
                    else:
                        if Q.der is None:
                            Q.der = node
                            break
                        Q = Q.der
        self.entry.delete(0, 'end')
        self.redraw()

    # ---------------- Expression parsing & tree ----------------
    def use_expression(self):
        expr = self.entry.get().strip()
        if expr == "":
            messagebox.showwarning("Entrada", "Escribe una expresión como 4-5/(7+8)^9 o letras.")
            return
        try:
            postfix = self._infix_to_postfix(expr)
            root = self._postfix_to_tree(postfix)
            self.root_node = root
            self.entry.delete(0, 'end')
            self.redraw()
        except Exception as e:
            messagebox.showerror("Parseo", f"Error parseando la expresión: {e}")

    def _infix_to_postfix(self, s):
        # Tokenize: numbers, identifiers (letters), operators, parentheses
        tokens = []
        i=0
        while i < len(s):
            c = s[i]
            if c.isspace():
                i+=1; continue
            if c.isdigit():
                num = c
                i+=1
                while i < len(s) and s[i].isdigit():
                    num += s[i]; i+=1
                tokens.append(num)
                continue
            if c.isalpha():
                ident = c
                i+=1
                while i < len(s) and s[i].isalnum():
                    ident += s[i]; i+=1
                tokens.append(ident)
                continue
            if c in "+-*/^()":
                tokens.append(c); i+=1; continue
            raise ValueError(f"Caracter inválido: {c}")
        # shunting-yard
        prec = {'^':4, '*':3, '/':3, '+':2, '-':2}
        right_assoc = {'^'}
        out=[]
        stack=[]
        for t in tokens:
            if t.isalnum():
                out.append(t)
            elif t in prec:
                while stack and stack[-1] in prec:
                    top = stack[-1]
                    if (prec[top] > prec[t]) or (prec[top]==prec[t] and t not in right_assoc):
                        out.append(stack.pop()); continue
                    break
                stack.append(t)
            elif t == '(':
                stack.append(t)
            elif t == ')':
                while stack and stack[-1] != '(':
                    out.append(stack.pop())
                if not stack or stack[-1] != '(':
                    raise ValueError("Paréntesis desbalanceados")
                stack.pop()
        while stack:
            if stack[-1] in '()':
                raise ValueError("Paréntesis desbalanceados")
            out.append(stack.pop())
        return out

    def _postfix_to_tree(self, postfix):
        stack=[]
        ops = set(['+','-','*','/','^'])
        for tok in postfix:
            if tok in ops:
                if len(stack) < 2:
                    raise ValueError("Expresión inválida")
                right = stack.pop()
                left = stack.pop()
                node = ExprNode(tok, left, right)
                stack.append(node)
            else:
                # operand: number or identifier
                try:
                    val = int(tok)
                except:
                    val = tok
                stack.append(ExprNode(val))
        if len(stack) != 1:
            raise ValueError("Expresión inválida")
        return stack[0]

    # ---------------- Drawing ----------------
    def redraw(self):
        self.canvas.delete("all")
        # reset node item mapping
        self.node_items = {}
        if self.root_node is None:
            self.status.config(text="Árbol vacío.")
            return
        # produce positions by inorder
        self.positions = {}
        self.x_counter = 0
        self._assign_coords(self.root_node, depth=0)
        width = max(800, (self.x_counter + 1) * self.x_gap + 60)
        height = max(300, (self._max_depth(self.root_node) + 2) * self.y_gap + 60)
        self.canvas.config(scrollregion=(0,0,width,height))
        self._draw_edges(self.root_node)
        self._draw_nodes()
        self.status.config(text=f"Nodos: {self.x_counter}")

    def _assign_coords(self, node, depth):
        if node is None:
            return
        self._assign_coords(node.izq, depth+1)
        x = self.x_counter * self.x_gap + 60
        y = depth * self.y_gap + 60
        self.positions[node] = (x,y)
        self.x_counter += 1
        self._assign_coords(node.der, depth+1)

    def _max_depth(self, node):
        if node is None:
            return 0
        return 1 + max(self._max_depth(node.izq), self._max_depth(node.der))

    def _draw_edges(self, node):
        if node is None:
            return
        if node.izq:
            x1,y1 = self.positions[node]; x2,y2 = self.positions[node.izq]
            self.canvas.create_line(x1, y1, x2, y2, width=2)
        if node.der:
            x1,y1 = self.positions[node]; x2,y2 = self.positions[node.der]
            self.canvas.create_line(x1, y1, x2, y2, width=2)
        self._draw_edges(node.izq)
        self._draw_edges(node.der)

    def _draw_nodes(self):
        for node, (x,y) in self.positions.items():
            r = self.node_radius
            oval = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="#ffd97d", outline="#333")
            text = self.canvas.create_text(x, y, text=str(node.info), font=("Segoe UI", 10, "bold"))
            self.node_items[node] = (oval, text)

    def show_inorden(self):
        if self.root_node is None:
            messagebox.showinfo("Inorden", "Árbol vacío.")
            return
        res=[]
        def inorder(n):
            if n is None: return
            inorder(n.izq); res.append(str(n.info)); inorder(n.der)
        inorder(self.root_node)
        messagebox.showinfo("Inorden", " ".join(res))

    # ---------------- Recorridos animados ----------------
    def _collect_inorder(self, node, out):
        if node is None: return
        self._collect_inorder(node.izq, out)
        out.append(node)
        self._collect_inorder(node.der, out)

    def _collect_preorder(self, node, out):
        if node is None: return
        out.append(node)
        self._collect_preorder(node.izq, out)
        self._collect_preorder(node.der, out)

    def _collect_postorder(self, node, out):
        if node is None: return
        self._collect_postorder(node.izq, out)
        self._collect_postorder(node.der, out)
        out.append(node)

    def start_traversal(self):
        if self.root_node is None:
            messagebox.showinfo("Recorrido", "Árbol vacío.")
            return
        if getattr(self, 'traversal_running', False):
            return
        choice = self.trav_choice.get()
        nodes = []
        if choice == "Inorden":
            self._collect_inorder(self.root_node, nodes)
        elif choice == "Preorden":
            self._collect_preorder(self.root_node, nodes)
        else:
            self._collect_postorder(self.root_node, nodes)
        # prepare animation: enable large traversal box and clear
        self.traversal_running = True
        self.btn_traverse.state(['disabled'])
        self.trav_result.config(text="")
        self.trav_large.config(state='normal')
        self.trav_large.delete('1.0', 'end')
        self.trav_large.tag_configure('center', justify='center')
        self._animate_traversal(nodes, 0, [])

    def _animate_traversal(self, nodes, idx, acc):
        if idx > 0:
            # restore previous node color
            prev = nodes[idx-1]
            if prev in self.node_items:
                oval, _ = self.node_items[prev]
                self.canvas.itemconfig(oval, fill="#ffd97d")
        if idx >= len(nodes):
            # finished
            self.traversal_running = False
            self.btn_traverse.state(['!disabled'])
            # lock large traversal box
            self.trav_large.config(state='disabled')
            return
        node = nodes[idx]
        # highlight current
        if node in self.node_items:
            oval, _ = self.node_items[node]
            self.canvas.itemconfig(oval, fill="#ff6b6b")
        acc.append(str(node.info))
        txt = " ".join(acc)
        self.trav_result.config(text=txt)
        # update large text box centered
        self.trav_large.config(state='normal')
        self.trav_large.delete('1.0', 'end')
        self.trav_large.insert('1.0', txt, 'center')
        self.trav_large.config(state='disabled')
        # schedule next
        self.after(650, lambda: self._animate_traversal(nodes, idx+1, acc))

    def clear(self):
        self.root_node = None
        self.canvas.delete("all")
        self.status.config(text="Árbol limpiado.")

if __name__ == "__main__":
    app = TreeApp()
    app.mainloop()