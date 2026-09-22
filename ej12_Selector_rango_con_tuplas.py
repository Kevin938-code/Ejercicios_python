"""Clase SelectorRango que: 
(1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango; 
(2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto."""
class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))
    
    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()
        for inicio, fin in rangos:
            elementos.update(self.crear_rango(inicio, fin))
        return sorted(elementos)
        
selector = SelectorRango()
print(selector.elementos_en_multiples_rangos((1, 3),(2, 4)))

print("-----------------------------------------------------------")
"""Ejercicio: SelectorPares

Crea una clase llamada SelectorPares que:

(1) Método crear_rango(inicio, fin)

Debe recibir un número inicial y uno final, y retornar una tupla que contenga únicamente los números pares dentro de ese rango, 
incluyendo el inicio y el fin cuando correspondan
(2) Método pares_en_multiples_rangos(*rangos)

Debe recibir varias tuplas, donde cada tupla representa:

(inicio, fin)
Debes:

Crear un set() vacío.
Recorrer todos los rangos recibidos.
Utilizar crear_rango() para obtener los pares de cada rango.
Agregar esos números al conjunto usando update().
Retornar una lista ordenada y sin duplicados.
"""
class SelectorPares:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))
    
    def pares_multiples_rangos(self, *rangos):
        pares = set ()
        
        for inicio, fin in rangos:
            pares.update(self.crear_rango(inicio, fin))
        return sorted(pares)

selector = SelectorPares()
selector.crear_rango(2, 6)
print(selector.pares_multiples_rangos((1, 3),(2, 4)))