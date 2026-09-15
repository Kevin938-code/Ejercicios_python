"""Clase AnalizadorNumeros que: 
(1) tenga método es_par(numero) que retorne True/False; 
(2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par; 
(3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares)."""
class AnalizadorNumeros:
    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        pares = []
        impares = []
        for numero in numeros:
            if self.es_par(numero):
                pares.append(numero)
            else:
                impares.append(numero)
        return {'pares': pares, 'impares': impares}

    def cantidad_pares_impares(self, *numeros):
        resultado = self.separar(*numeros)
        cant_pares = len(resultado['pares'])
        cant_impares = len(resultado['impares'])
        return (cant_pares, cant_impares)

numero = AnalizadorNumeros()
print(numero.es_par(4))
print(numero.separar(1, 2, 3, 4, 5))
print(numero.cantidad_pares_impares(1, 2, 3, 4, 5))
