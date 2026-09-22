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

print("-----------------------------------------------------")

"""Ejercicio: AnalizadorEdades
Crea una clase llamada AnalizadorEdades que trabaje con varias edades.
    1. Método es_mayor_edad(edad)
Debe recibir una edad y retornar:
True si la edad es 18 o mayor.
False si es menor de 18.
    2. Método separar(*edades)
Debe recibir varias edades y reutilizar es_mayor_edad().
Debe separar las edades en dos listas Y retornar un diccionario
    3. Método cantidad_mayores_menores()
Debe retornar una tupla
"""
class AnalizadorEdades:
    def __init__(self):
        self.mayores = []
        self.menores = []

    def es_mayor_edad(self, edad):
        return edad >= 18

    def separar(self, *edades):
        
        for edad in edades:
            if self.es_mayor_edad(edad):
                self.mayores.append(edad)
            else:
                self.menores.append(edad)
        return {'mayor edad': self.mayores, 'menor edad': self.menores}
    
    def cantidad_mayores_menores(self):
        return len(self.mayores), len(self.menores)
    
analiza = AnalizadorEdades()
print(analiza.es_mayor_edad(18))
print(analiza.separar(10, 20, 13, 40, 15))
print(analiza.cantidad_mayores_menores())

