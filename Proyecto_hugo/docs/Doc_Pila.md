Propósito
- Implementación sencilla de una pila (`Pila`) usada por `Arbol_expresiones`.

Métodos principales
- `reiniciar()`: vacía la pila.
- `insertar(dato)`: apila un `dato` en la cima.
- `eliminar()`: desapila y devuelve el dato de la cima.
- `pila_vacia()`: True si la pila está vacía.
- `cima_pila()`: devuelve el dato de la cima sin eliminarlo.
- `imprime()`: devuelve una cadena con los elementos (no modifica permanentemente la pila).

Uso
- Crear: `p = Pila(); p.insertar(3); x = p.eliminar()`.

Notas
- La implementación usa nodos `nodoPila` con campos `dato` y `siguiente`.
- Es muy adecuada para construir árboles desde notación postfija.