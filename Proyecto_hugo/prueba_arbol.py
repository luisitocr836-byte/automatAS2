from albol import Arbol_expresiones

expr =str(input("Ingrese la expresión en notación: "))

arb = Arbol_expresiones()
arb.construir_desde_infija(expr)

print("Preorden:", arb.recorrido_preorden())
print("Inorden:", arb.recorrido_inorden())
print("Postorden:", arb.recorrido_postorden())
#lalo te toca hacer todo el proyeto

