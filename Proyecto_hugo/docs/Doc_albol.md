Propósito
- Clase `Arbol_expresiones` para construir y obtener recorridos de un árbol de expresiones.

Funcionalidad principal
- `construir_desde_infija(expresion_infija)`: toma una cadena infija (con paréntesis) y construye el árbol internamente.
  - Tokeniza la expresión, convierte a postfija y llama a `construir_desde_postfija`.
- `construir_desde_postfija(expresion_postfija)`: espera tokens separados por espacios en notación postfija; construye árbol usando `Pila` y nodos `ArbolBB`.
- Recorridos:
  - `recorrido_preorden()`, `recorrido_inorden()`, `recorrido_postorden()` — devuelven una cadena con el recorrido.

Notas de uso
- Para `construir_desde_postfija` pasar algo como: "3 4 + 5 *".
- Para `construir_desde_infija` pasar una expresión normal: "(3+4)*5".
- La clase usa `Libreria.Pila.pila.Pila` y `Libreria.edNoLineales.ArbolBB.ArbolBB` para nodos y recorridos.

Ejemplo
- `arb = Arbol_expresiones(); arb.construir_desde_infija("(3+4)*5"); print(arb.recorrido_postorden())`