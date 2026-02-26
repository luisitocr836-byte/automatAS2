# Presentación - Árbol de Expresiones (7 minutos)

## 1. ¿QUÉ ES EL PROYECTO? (1 min)

Una **aplicación gráfica en Tkinter** que:
- Parsea expresiones matemáticas infijas (ej: `4-5/(7+8)^9`)
- Construye un **árbol de expresión** que representa la estructura de la expresión
- Visualiza el árbol gráficamente
- Anima los **tres tipos de recorridos**: Inorden, Preorden, Postorden

---

## 2. COMPONENTES PRINCIPALES (1.5 min)

### Classes:

**ExprNode** - Nodo compatible con ArbolBB
```python
class ExprNode:
    def __init__(self, info, izq=None, der=None)
        self.info = info   # Operando u operador
        self.izq = izq     # Hijo izquierdo
        self.der = der     # Hijo derecho
```

**ArbolConAnimacion** - Extiende ArbolBB
```python
class ArbolConAnimacion(ArbolBB):
    # Hereda métodos preorden, inorden, postorden
    # MODIFICACIÓN: retorna lista de nodos para la animación
    # ArbolBB HACE el recorrido + CAPTURA nodos simultáneamente
```

**TreeApp** - Interfaz gráfica principal
- Entrada de expresiones
- Canvas para visualizar el árbol
- Selector de recorridos y botón de animación

---

## 3. FLUJO DE PROCESAMIENTO (2 min)

### Paso 1: Usuario escribe expresión
```
Entrada: "a+b*c"
```

### Paso 2: Conversión Infija → Postfija (Shunting Yard)
```
Infija:   a + b * c
Postfija: a b c * +
```
- Respeta precedencias: `^ (potencia) > *, / > +, -`
- La potencia es **asociativa por la derecha**: `2^3^2 = 2^(3^2) = 512`

### Paso 3: Postfija → Árbol de Expresión
```
Postfija: [a, b, c, *, +]
           
        Usa PILA:
        - a → [a]
        - b → [a, b]
        - c → [a, b, c]
        - * → [a, (b*c)]      ← pop dos, crea nodo operador
        - + → [(a+(b*c))]     ← pop dos, crea nodo raíz

Resultado:
           +
          / \
         a   *
            / \
           b   c
```

### Paso 4: Dibujar en Canvas
- **Posicionamiento**: Usa recorrido **inorden** para distribuir nodos horizontalmente
- **Profundidad**: Calcula automáticamente la altura del árbol
- **Aristas**: Dibuja líneas desde padre a hijos
- **Nodos**: Círculos con el valor del operando/operador

---

## 4. RECORRIDOS CON ARBOLBB (1.5 min)

### ¿Cómo trabajan juntos ArbolBB y arbolProvisional?

**ArbolConAnimacion (hereda de ArbolBB):**
```python
def postorden(self, Q, nodos=None):
    if Q is not None:
        self.postorden(Q.izq, nodos)      # Recorre izquierda
        self.postorden(Q.der, nodos)      # Recorre derecha
        nodos.append(Q)                   # ✓ CAPTURA para animación
        self.listABB += " " + str(Q.info) # ✓ CONCATENA (como ArbolBB original)
    return nodos
```

**Result:**
1. **ArbolBB IMPLEMENTA** el recorrido (ya que no podemos modificar ArbolBB.py)
2. **ArbolConAnimacion EXTIENDE** los métodos para CAPTURAR nodos simultáneamente
3. **arbolProvisional ANIMA** los nodos capturados con retrasos de 650ms

**Ventaja**: No duplicamos la lógica del algoritmo, solo agregamos captura de nodos

### Los tres recorridos:

| Orden | Patrón | Ejemplo |
|-------|--------|---------|
| **Preorden** | Raíz → Izq → Der | `+ a * b c` |
| **Inorden** | Izq → Raíz → Der | `a + b * c` (vuelve a la expresión original) |
| **Postorden** | Izq → Der → Raíz | `a b c * +` (notación postfija) |

---

## 5. ANIMACIÓN Y VISUALIZACIÓN (0.5 min)

Cuando el usuario selecciona un recorrido y presiona "Recorrer":

1. **Se obtienen los nodos** en el orden especificado (usando ArbolConAnimacion)
2. **Cada 650ms**:
   - Colorea el nodo actual en **rojo**
   - Acumula y muestra el resultado
   - Colorea el nodo anterior en **amarillo** (reset)
3. **Al terminar**: Todos los nodos vuelven al color original

```
Ejemplo Postorden: a b c * +
Animación:
[a] →  [a, b] → [a, b, c] → [a, b, c, *] → [a, b, c, *, +]
```

---

## 6. CÓDIGO SIN DUPLICACIÓN - LA CLAVE (1 min)

### Problema inicial:
```
ArbolBB.postorden() no retorna nodos
       ↓
Necesitamos capturar nodos para animación
       ↓
Opción 1: Recorrer DOS VECES (ineficiente) ❌
Opción 2: Modificar ArbolBB.py (prohibido) ❌
Opción 3: Heredar y extender métodos ✅
```

### Solución elegante:
```python
class ArbolConAnimacion(ArbolBB):  # Hereda de ArbolBB
    def postorden(self, Q, nodos=None):
        # Mismo algoritmo que ArbolBB
        # + retorna nodos capturados
```

**Ventajas:**
- ✅ Reutilizamos la lógica de ArbolBB
- ✅ No modificamos ArbolBB.py
- ✅ Una sola pasada por el árbol
- ✅ Código limpio y mantenible

---

## RESUMEN FINAL

| Aspecto | Tecnología |
|---------|-----------|
| **Interfaz** | Tkinter (GUI multiplataforma) |
| **Parseo** | Algoritmo Shunting Yard |
| **Árbol** | ExprNode (compatible con ArbolBB) |
| **Recorridos** | ArbolConAnimacion (extiende ArbolBB) |
| **Animación** | Canvas + tkinter.after() (250ms) |
| **Visualización** | Posicionamiento inorden automático |

---

## DEMOSTRACIÓN RECOMENDADA

1. Escribir: `2+3*5^2`
2. Click "Usar Expresión" → muestra el árbol
3. Seleccionar "Inorden" → Click "Recorrer" → muestra: `2 + 3 * 5 ^ 2`
4. Seleccionar "Postorden" → Click "Recorrer" → muestra: `2 3 5 2 ^ * +`
5. Señalar en pantalla cómo ArbolBB hace el recorrido y arbolProvisional anima

---

**NOTAS FINALES:**
- La aplicación es **agnóstica**: funciona tanto con ExprNode como con ArbolBB
- Si el árbol es ArbolBB → usa ArbolConAnimacion
- Si es ExprNode → usa _recorrer_generico()
- Código flexible y reutilizable
