class PilaSemantica:
    def __init__(self):
        self.pila = []  # TAMAÑO ILIMITADO
    
    def push(self, valor, tipo):
        self.pila.append((valor, tipo))
        self.mostrar()
    
    def pop(self, cantidad=1):
        elementos = []
        for _ in range(cantidad):
            if self.pila:
                elementos.append(self.pila.pop())
        return elementos
    
    def mostrar(self):
        if not self.pila:
            print("  [ VACÍA ]")
            return
        pila_str = []
        for v, t in reversed(self.pila):
            pila_str.append(f"{v}:{t}")
        print("  " + " | ".join(pila_str))


def evaluar():
    
    expresion = input("  🧮 INGRESA TU EXPRESIÓN: ")
    
    
    pila = PilaSemantica()
    postfijo = []
    ops = []
    precedencia = {'+':1, '-':1, '*':2, '/':2, '(':0}
    
    # === CONVERTIR INFIX A POSTFIJO ===
    print("\n📦 CONVIRTIENDO A NOTACIÓN POSTFIJA...")
    tokens = []
    i = 0
    while i < len(expresion):
        c = expresion[i]
        if c == ' ':
            i += 1
            continue
        if c.isdigit():
            num = c
            while i+1 < len(expresion) and expresion[i+1].isdigit():
                i += 1
                num += expresion[i]
            tokens.append(int(num))
        elif c in '+-*/()':
            tokens.append(c)
        i += 1
    
    for token in tokens:
        if isinstance(token, int):
            pila.push(token, 'ent')
            postfijo.append(token)
        elif token == '(':
            ops.append('(')
        elif token == ')':
            while ops and ops[-1] != '(':
                postfijo.append(ops.pop())
            ops.pop()
        else:
            while ops and ops[-1] != '(' and precedencia.get(ops[-1], 0) >= precedencia[token]:
                postfijo.append(ops.pop())
            ops.append(token)
    
    while ops:
        postfijo.append(ops.pop())
    
    print(f"  📝 POSTFIJO: {[p if isinstance(p, int) else p for p in postfijo]}")
    
    # === PROCESAR OPERACIONES ===
    print("\n⚙️  PROCESANDO OPERACIONES...")
    for token in postfijo:
        if isinstance(token, int):
            continue
        if token in '+-*/':
            b = pila.pop(1)[0][0]
            a = pila.pop(1)[0][0]
            
            if token == '+': r = a + b
            elif token == '-': r = a - b
            elif token == '*': r = a * b
            elif token == '/': 
                if b == 0:
                    print("  ❌ ERROR: División por cero")
                    return
                r = a / b
            
            print(f"  🔢 CALC: {a} {token} {b} = {r}")
            pila.push(r, 'ent')
    
    # === RESULTADO FINAL ===
    print("\n" + "═"*60)
    if pila.pila:
        print(f"  ✅ RESULTADO FINAL: {pila.pila[0][0]}")
    else:
        print("  ❌ ERROR: No hay resultado")
    print("═"*60)


# ============================================================
#  🎯 EJECUTAR - ESCRIBE CUALQUIER EXPRESIÓN
# ============================================================

while True:
    evaluar()
    print("\n¿Otra expresión? (Enter para continuar, 'q' para salir)")
    if input().lower() == 'q':
        break