Propósito
- `ArbolBB` es una clase que representa nodos de un árbol binario de búsqueda y provee métodos básicos.

Atributos importantes
- `info`: dato almacenado en el nodo.
- `izq`, `der`: referencias a hijos izquierdo y derecho.
- `P`: cabecera (nodo contenedor) creada por `crea_cab()`.
- `listABB`: cadena acumuladora usada por los métodos de recorrido.

Métodos principales
- `crea_cab()`: crea `self.P` como cabecera del árbol.
- `insertar(tipo)`: inserta un nuevo nodo; pide al usuario el valor (usa el `tipo` para convertir input).
- `preorden(Q)`, `inorden(Q)`, `postorden(Q)`: recorridos recursivos que concatenan resultados en `listABB`.
- `elimina1()`, `elimina2(R)`: elimina un dato pedido por el usuario; `elimina2` realiza la lógica de sustitución.
- `buscar(Q)`: busca `self.x` en el árbol y marca `self.b` cuando lo encuentra.

Uso básico
- Crear y preparar: `obj = ArbolBB(None,None,None); obj.crea_cab()`.
- Insertar (desde el menú principal) o adaptar `insertar` para pasar valores programáticamente.

Notas
- Muchos métodos usan `input()` y `print()`: están diseñados para interacción por consola.
- Para usar la clase en código no interactivo, adaptar los métodos de inserción y eliminación para aceptar parámetros en lugar de `input()`.