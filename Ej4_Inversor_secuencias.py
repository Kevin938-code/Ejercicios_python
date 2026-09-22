"""Clase InversorSecuencia que: 
(1) tenga método invertir_lista(lista) que retorne la lista invertida sin usar reversed() (usa manual con bucles); 
(2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir varias listas y retorne un diccionario {lista_original: lista_invertida}."""

class InversorSecuencia:
    def invertir_lista(self, lista):
        lista_invertida = []
        for i in range(len(lista) -1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida

    def invertir_multiples(self, *listas):
        diccionario_invertido = {}
        for lista in listas:
            diccionario_invertido[tuple(lista)] = self.invertir_lista(lista)
            return diccionario_invertido

invertido = InversorSecuencia()
print(invertido.invertir_lista([1, 2, 3, 4, 5]))
print(invertido.invertir_multiples([1, 2, 3], ['a', 'b', 'c']))


print("------------------------------------------------------------")
"""Ejercicio: Clase AnalizadorListas
Crea una clase llamada AnalizadorListas que trabaje con varias listas de números.
    1. mayor_lista(lista)
Debe recibir una lista de números y retornar el número mayor, pero hay una condición:
No puedes utilizar max().
Debes encontrar el mayor utilizando un bucle manualmente.
    2. analizar_multiples(*listas)
Debe recibir varias listas y reutilizar mayor_lista() para encontrar el mayor de cada una."""

class AnalizadorListas:
    def mayor_lista(self, lista):
        mayor = lista[0]
        for numero in lista:
            if numero > mayor:
                mayor = numero
        return mayor

    def analizar_multiples(self, *listas):
        diccionario_lista = {}
        for lista in listas:
            diccionario_lista[tuple(lista)]=self.mayor_lista(lista)
        return diccionario_lista

analizar = AnalizadorListas()
print(analizar.mayor_lista([1,5,3,4]))
print(analizar.analizar_multiples([1,5,3,4], [10,20,5],[5,7]))