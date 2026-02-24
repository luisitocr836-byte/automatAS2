Propósito
- Interfaz gráfica (Tkinter) que permite:
  - Insertar valores como BST (enteros o texto).
  - Parsear expresiones infijas (ej. 4-5/(7+8)^9) y mostrar el árbol de expresión.
  - Dibujar el árbol y animar recorridos (inorden, preorden, postorden).

Componentes principales
- `TreeApp` (Tkinter): entrada, botones, canvas para dibujo.
- `ExprNode`: nodo simple con `info`, `izq`, `der` compatible con `ArbolBB`.
- Funciones clave:
  - `insert_bst()`: inserta un nodo en un BST existente o crea uno nuevo.
  - `use_expression()`: convierte infija→postfija y construye árbol de expresiones.
  - `_infix_to_postfix()` y `_postfix_to_tree()`: parser básico (operadores ^,*,/,+,- y paréntesis).
  - `redraw()`: calcula posiciones y dibuja nodos y aristas.
  - `start_traversal()` y `_animate_traversal()`: recorre y destaca nodos.

Uso rápido
- Ejecutar el archivo: `python arbolProvisional.py` (ejecuta la ventana Tk).
- En la caja de entrada, escribir un número/letra y presionar "Insertar (BST)" o escribir una expresión y presionar "Usar Expresión".

Notas
- El parser acepta números enteros y identificadores alfanuméricos.
- Si la raíz actual es un árbol de expresiones y se inserta como BST, reemplaza la raíz por el nuevo nodo BST.
- El código dibuja nodos usando referencias por objeto; no persiste a disco.