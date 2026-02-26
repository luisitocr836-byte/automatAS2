# Documentación de arbolProvisional.py

## Descripción General
`arbolProvisional.py` es una aplicación gráfica basada en **Tkinter** que permite:
- Insertar valores en un **Árbol Binario de Búsqueda (BST)** con números o letras
- Parsear **expresiones matemáticas infijas** (ej. `4-5/(7+8)^9`) y convertirlas en árboles de expresión
- Visualizar el árbol de forma gráfica en un canvas
- Realizar y animar **tres tipos de recorridos**: Inorden, Preorden, Postorden

---

## Clases

### Clase `ExprNode`
Representa un **nodo genérico** compatible con `ArbolBB` para árboles de expresiones.

#### Atributos:
- `info`: Almacena el valor del nodo (número, variable u operador)
- `izq`: Referencia al hijo izquierdo (o `None`)
- `der`: Referencia al hijo derecho (o `None`)

#### Métodos:
- `__init__(self, info, izq=None, der=None)`: Inicializa un nodo con un valor y referencias opcionales a hijos

---

### Clase `TreeApp(tk.Tk)`
Aplicación principal que hereda de `Tkinter.Tk` y gestiona toda la interfaz gráfica y lógica del árbol.

#### Atributos de instancia:
- `nodo_raiz`: Referencia a la raíz actual del árbol (puede ser `ArbolBB` o `ExprNode`)
- `entry`: Widget de entrada de texto para el usuario
- `canvas`: Canvas para dibujar el árbol visualmente
- `opcion_recorrido`: ComboBox para seleccionar el tipo de recorrido (Inorden/Preorden/Postorden)
- `btn_recorrer`: Botón para iniciar la animación del recorrido
- `resultado_recorrido`: Label para mostrar el recorrido actual (línea)
- `recorrido_grande`: Text widget para mostrar el recorrido en grande (pantalla grande)
- `x_gap`, `y_gap`: Espacios horizontales y verticales entre nodos en el canvas
- `node_radius`: Radio de los círculos de los nodos
- `positions`: Diccionario que almacena las coordenadas (x, y) de cada nodo
- `node_items`: Diccionario que mapea nodos a sus representaciones gráficas (óval + texto)
- `recorrido_ejecutandose`: Bandera que indica si hay una animación en progreso

---

## Métodos de la clase `TreeApp`

### `__init__(self)`
**Propósito**: Inicializa la ventana principal y llama a la construcción de la interfaz.

**Qué hace**:
1. Configura el título de la ventana a "Árbol: BST y Expresiones"
2. Establece el tamaño a 1000x650 píxeles
3. Inicializa `nodo_raiz` a `None` (árbol vacío)
4. Llama a `_build_ui()` para construir la interfaz
5. Define espacios y radio para el dibujo de nodos

---

### `_build_ui(self)`
**Propósito**: Construye toda la interfaz gráfica con botones, campos de entrada, canvas y displays.

**Qué hace**:
1. **Barra superior**: Crea un frame con:
   - Etiqueta "Entrada:"
   - Campo de texto (`entry`) para escribir valores o expresiones
   - Botón "Insertar (BST)" → llama a `insertar_bst()`
   - Botón "Usar Expresión" → llama a `usar_expresion()`
   - Botón "Limpiar" → llama a `limpiar()`
   - Botón "Redibujar" → llama a `redibujar()`
   - Botón "Mostrar Inorden" → llama a `mostrar_inorden()`
   - ComboBox para seleccionar recorrido (Inorden/Preorden/Postorden)
   - Botón "Recorrer" → llama a `iniciar_recorrido()`
   - Etiqueta y Label para mostrar el recorrido actual

2. **Área de recorrido grande**: Un Text widget de 4 líneas que muestra el recorrido completo y centrado

3. **Canvas principal**: Área blanca donde se dibuja el árbol

4. **Barra de estado**: Label inferior que muestra información (árbol vacío, número de nodos, etc.)

---

### `insertar_bst(self)`
**Propósito**: Inserta un valor en el árbol binario de búsqueda.

**Qué hace**:
1. Obtiene el texto del campo `entry`
2. Si está vacío, muestra advertencia
3. Crea una instancia de `ArbolBB` como contenedor
4. Inicializa la cabecera del árbol con `crea_cab()`
5. Asigna el árbol actual a la cabecera (`arb.P.izq = self.nodo_raiz`)
6. Determina si convertir la entrada a `int` o mantenerla como `str`
7. **Truco importante**: Reemplaza temporalmente la función `input()` de Python para que devuelva el texto de la caja de entrada
8. Llama al método `insertar(tipo)` de `ArbolBB` (que internamente usa la función `input` parcheada)
9. Restaura la función `input()` original
10. Actualiza `self.nodo_raiz` con el árbol resultante
11. Limpia el campo de entrada y redibuja el árbol

**Reutilización**: Usa directamente el código de `ArbolBB.insertar()` sin modificar ese archivo.

---

### `usar_expresion(self)`
**Propósito**: Parsea una expresión matemática infija y construye un árbol de expresión.

**Qué hace**:
1. Obtiene el texto del campo `entry`
2. Si está vacío, muestra advertencia
3. Intenta convertir la expresión infija a postfija con `_infija_a_postfija()`
4. Convierte la notación postfija a un árbol con `_postfija_a_arbol()`
5. Asigna el árbol generado a `self.nodo_raiz`
6. Limpia el campo de entrada y redibuja

**Ejemplo**:
- Entrada: `4-5/(7+8)^9`
- Salida: Un `ExprNode` que representa la expresión en forma de árbol

---

### `_infija_a_postfija(self, cadena)`
**Propósito**: Convierte una expresión matemática de notación infija a postfija usando el algoritmo **Shunting Yard**.

**Qué hace**:
1. **Tokenización**: Escanea la cadena y divide en tokens:
   - Números multidígito (ej. `123`)
   - Identificadores alfanuméricos (ej. `x`, `var`)
   - Operadores: `+, -, *, /, ^`
   - Paréntesis: `(, )`
   
2. **Algoritmo Shunting Yard**:
   - Usa una pila para operadores y paréntesis
   - Usa una lista de salida para el resultado
   - Define precedencias: `^=4, *=/=3, +-=-2`
   - La potencia `^` es asociativa por la derecha (a^b^c = a^(b^c))
   
3. Valida paréntesis balanceados

4. Retorna la lista con la expresión en notación postfija

**Ejemplo**:
- Entrada: `a+b*c`
- Salida: `['a', 'b', 'c', '*', '+']`

---

### `_postfija_a_arbol(self, postfija)`
**Propósito**: Construye un árbol de expresión a partir de una expresión en notación postfija.

**Qué hace**:
1. Usa una pila para almacenar nodos
2. **Por cada token en postfija**:
   - Si es operador (`+, -, *, /, ^`):
     - Saca dos nodos de la pila (derecho, izquierdo)
     - Crea un nuevo `ExprNode` con el operador como raíz y los dos nodos como hijos
     - Coloca el nuevo nodo en la pila
   - Si es operando (número o variable):
     - Crea un `ExprNode` con ese valor
     - Lo coloca en la pila

3. Al final, la pila debe contener exactamente un nodo (la raíz del árbol)
4. Si no, lanza error "Expresión inválida"

**Ejemplo**:
- Entrada: `['a', 'b', '+']`
- Salida: Un `ExprNode` con `+` como raíz y `a`, `b` como hijos

---

### `redibujar(self)`
**Propósito**: Borra el canvas anterior y dibuja el árbol completo.

**Qué hace**:
1. Limpia el canvas de dibujos previos
2. Reinicia el diccionario `node_items`
3. Si el árbol está vacío, muestra mensaje y retorna
4. Inicializa un diccionario `positions` (vacío) y contador `x_counter`
5. Llama a `_asignar_coords()` para calcular posiciones de cada nodo
6. Calcula el tamaño mínimo necesario del canvas basado en:
   - Número de nodos (`x_counter`)
   - Profundidad máxima del árbol
7. Dibuja las aristas (líneas entre nodos) con `_dibujar_aristas()`
8. Dibuja los nodos (círculos con números) con `_dibujar_nodos()`
9. Actualiza el status mostrando el número total de nodos

---

### `_asignar_coords(self, nodo, depth)`
**Propósito**: Calcula las coordenadas (x, y) de cada nodo usando un recorrido **inorden**.

**Qué hace**:
1. Recursivamente recorre el árbol en **inorden**:
   - Primero: hijo izquierdo
   - Luego: nodo actual
   - Finalmente: hijo derecho

2. Para cada nodo:
   - Calcula `x = contador * x_gap + offset`
   - Calcula `y = profundidad * y_gap + offset`
   - Almacena en `self.positions[nodo] = (x, y)`
   - Incrementa el contador

3. Esta estrategia distribuye los nodos de izquierda a derecha siguiendo el orden inorden

---

### `_profundidad_maxima(self, nodo)`
**Propósito**: Calcula recursivamente la profundidad máxima del árbol.

**Qué hace**:
1. Si el nodo es `None`, retorna 0
2. Si no, retorna 1 + max(profundidad del subárbol izquierdo, profundidad del subárbol derecho)

**Resultado**: Número de niveles del árbol

---

### `_dibujar_aristas(self, nodo)`
**Propósito**: Dibuja las líneas (aristas) conectando nodos padre con hijos.

**Qué hace**:
1. Si el nodo es `None`, retorna
2. Si existe hijo izquierdo:
   - Obtiene las coordenadas del nodo actual y del hijo izquierdo
   - Dibuja una línea entre ellas
3. Si existe hijo derecho:
   - Obtiene las coordenadas y dibuja la línea
4. Recursivamente dibuja aristas de los subárboles izquierdo y derecho

---

### `_dibujar_nodos(self)`
**Propósito**: Dibuja los círculos (óvalos) con números que representan los nodos.

**Qué hace**:
1. **Por cada nodo** en el diccionario `positions`:
   - Obtiene sus coordenadas (x, y)
   - Dibuja un óvalo (círculo) de color amarillo (#ffd97d) con borde negro
   - Coloca un texto en el centro con el valor del nodo
   - Almacena la referencia gráfica (óval, texto) en `node_items` para poder colorearse después

---

### `mostrar_inorden(self)`
**Propósito**: Muestra un diálogo con la cadena de recorrido inorden del árbol.

**Qué hace**:
1. Verifica si el árbol está vacío
2. Crea una instancia temporal de `ArbolBB`
3. Reinicia el acumulador `arb.listABB = ""`
4. Ejecuta el método `inorden()` de `ArbolBB` sobre el nodo raíz
5. Muestra el resultado en un diálogo MessageBox

**Reutilización**: Usa directamente el método `inorden()` de la clase `ArbolBB` sin modificación.

---

### `_colectar_inorden(self, nodo, lista)`
**Propósito**: Recorre el árbol en inorden acumulando los nodos (no strings) en una lista.

**Qué hace**:
1. Recursivamente en orden **inorden**:
   - Izq → Nodo → Der
2. En lugar de concatenar strings, **agrega el nodo mismo** a la lista
3. Esta lista se usa luego para la animación del recorrido

---

### `_colectar_preorden(self, nodo, lista)`
**Propósito**: Recorre el árbol en preorden acumulando los nodos en una lista.

**Qué hace**:
1. Recursivamente en orden **preorden**:
   - Nodo → Izq → Der
2. Agrega el nodo a la lista
3. Se usa para la animación del recorrido preorden

---

### `_colectar_postorden(self, nodo, lista)`
**Propósito**: Recorre el árbol en postorden acumulando los nodos en una lista.

**Qué hace**:
1. Recursivamente en orden **postorden**:
   - Izq → Der → Nodo
2. Agrega el nodo a la lista
3. Se usa para la animación del recorrido postorden

---

### `iniciar_recorrido(self)`
**Propósito**: Inicia la animación del recorrido seleccionado (Inorden, Preorden o Postorden).

**Qué hace**:
1. Verifica si el árbol está vacío
2. Verifica si ya hay una animación en progreso (evita múltiples animaciones simultáneas)
3. Obtiene el tipo de recorrido seleccionado del ComboBox
4. Colecta los nodos en el orden especificado:
   - Si "Inorden": llama `_colectar_inorden()`
   - Si "Preorden": llama `_colectar_preorden()`
   - Si "Postorden": llama `_colectar_postorden()`
5. Marca la bandera `recorrido_ejecutandose = True`
6. Deshabilita el botón "Recorrer" para evitar múltiples ejecuciones
7. Limpia los displays de recorrido
8. Configura el Text widget para aceptar actualizaciones
9. Inicia la animación llamando a `_animar_recorrido()`

---

### `_animar_recorrido(self, nodos, idx, acumulado)`
**Propósito**: Anima la ejecución del recorrido, coloreando nodos de uno en uno con un delay.

**Qué hace**:
1. **Si idx > 0** (no es el primer nodo):
   - Obtiene el nodo anterior
   - Si está visible en `node_items`, lo colorea de amarillo (#ffd97d) para resetear

2. **Si idx >= len(nodos)** (recorrido completado):
   - Marca `recorrido_ejecutandose = False`
   - Habilita nuevamente el botón "Recorrer"
   - Desactiva el Text widget de resultado
   - Retorna

3. **En cada paso**:
   - Obtiene el nodo actual (nodos[idx])
   - Si está visible, lo colorea de rojo (#ff6b6b)
   - Agrega el valor del nodo a `acumulado`
   - Crea una cadena con todos los acumulados separados por espacios
   - Actualiza el Label de recorrido actual y el Text widget grande
   - Deshabilita el Text widget
   - Programa la siguiente iteración con `after(650ms)`

4. **Recursión**: Se llama a sí misma cada 650ms para el siguiente nodo

---

### `limpiar(self)`
**Propósito**: Limpia el árbol y la visualización.

**Qué hace**:
1. Asigna `nodo_raiz = None`
2. Borra todo lo dibujado en el canvas
3. Actualiza el estado a "Árbol limpiado."

---

## Flujo de uso típico

1. **Insertar en BST**:
   - Usuario escribe `5` en el campo entry
   - Click en "Insertar (BST)"
   - Se crea/actualiza el árbol binario de búsqueda
   - El árbol se redibuja

2. **Parsear expresión**:
   - Usuario escribe `a+b*c`
   - Click en "Usar Expresión"
   - Se convierte a postfija: `a b c * +`
   - Se construye el árbol de expresión
   - Se redibuja

3. **Animar recorrido**:
   - Usuario selecciona "Preorden" del ComboBox
   - Click en "Recorrer"
   - Cada 650ms se colorea un nodo rojo, se acumula y muestra
   - Al final, todos los nodos están amarillos nuevamente

---

## Dependencias externas

- `tkinter`: GUI (stdlib)
- `ArbolBB` de `Libreria.edNoLineales.ArbolBB`: Para la inserción en BST y recorridos

---

## Notas técnicas

El código **reutiliza** la clase `ArbolBB` de forma inteligente:
- Para inserción: Parcheando la función `input()` global
- Para recorridos: Copiando la lógica de recorrido sin modificar el archivo original
- Esto permite mantener `ArbolBB` intacto mientras se aprovecha su implementación
