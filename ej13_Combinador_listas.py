"""Clase CombinadorListas que: 
(1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; 
(2) tenga método intercalar_multiples(*listas) que reutilice para varias listas."""
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        combinar = []
        mas_largo = max(len(lista1), len(lista2))
        for i in range(mas_largo):
            if i < len(lista1):
                combinar.append(lista1[i])
            if i < len(lista2):
                combinar.append(lista2[i])
        return combinar

    def intercalar_multiples(self, *listas):
        combinar = []
        mas_largo = max(len(l) for l in listas)
        for i in range(mas_largo):
            for lista in listas :
                if i < len(listas):
                    combinar.append(lista[i])
        return combinar

combinador = CombinadorListas()
print(combinador.intercalar([1, 2], [3, 4]))
print(combinador.intercalar_multiples([1, 2], [3, 4], [5, 6]))

print("--------------------------------------------------------------------------")
"""Ejercicio: UnidorListas

Crea una clase llamada UnidorListas que:

(1) Método unir(lista1, lista2)

Debe recibir dos listas y crear una nueva lista colocando primero todos los elementos de lista1 y después todos los elementos de lista2.
unidor.unir([1, 2], [3, 4])
Importante: intenta hacerlo utilizando un for y append()
(2) Método unir_multiples(*listas)

Debe recibir varias listas y reutilizar el método unir() para combinarlas.
"""
class UnidorListas:

    def unir(self, lista1, lista2):
        resultado = []
        for elemento in lista1:
            resultado.append(elemento)
        for elemento in lista2:
            resultado.append(elemento)
        return resultado

    def unir_multiples(self, *listas):
        resultado = []

        for lista in listas:
            resultado = self.unir(resultado, lista)
        return resultado

union = UnidorListas()
print(union.unir([1, 2], [3, 4]))
print(union.unir_multiples([1, 2], [3, 4], [5, 6]))