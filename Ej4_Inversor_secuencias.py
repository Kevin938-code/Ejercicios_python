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