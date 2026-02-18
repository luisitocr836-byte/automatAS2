from albol import Arbol_expresiones

expr =str(input("Ingrese la expresión en notación: "))

arb = Arbol_expresiones()
arb.construir_desde_infija(expr)

print("Preorden:", arb.recorrido_preorden())
print("Inorden:", arb.recorrido_inorden())
print("Postorden:", arb.recorrido_postorden())
#lalo te toca hacer todo el proyeto
# ora que proyecto ?
# El de papi jacobo, mañana tenemos que llegar con una pizza
# vavavavavvaavava mita y mita
# vamos por ella o la pedimos a domicilio, ya que el profe no se aguita que lleguemos con comida, le damos dos y ya
#pues es que, no creo que nos de tiempo a ir por la pizza, mejor la pedimos a domicilio, y ya que el profe no se aguita, le damos dos rebanadas y ya
# orale va, mañana pedimos la pizza  ademas mañana no voy a dejar a lore y mañana si nos fumamos un cigarro