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