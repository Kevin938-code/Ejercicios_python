"""Clase DivisorFinder que: 
(1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores; 
(2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; 
(3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}"""
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0 :
                divisores.append(i)
        return tuple(divisores)
    
    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = sum(divisor for divisor in divisores if divisor != numero)
        return suma == numero
    
    def encontrar_multiples_divisores(self, *numeros):
        return {numero: self.encontrar_divisores(numero) for numero in numeros}
    
div = DivisorFinder()
print(div.encontrar_divisores(12))
print(div.es_perfecto(28))
print(div.encontrar_multiples_divisores(6, 12, 18, 24))

print("---------------------------------------------------------------------")
"""Ejercicio: FactorialFinder

Crea una clase llamada FactorialFinder que:

(1) Método calcular_factorial(numero)

Debe calcular y retornar el factorial de un número.
(2) Método es_factorial_par(numero)

Debe utilizar el método anterior para calcular el factorial y retornar:

True si el factorial es par.
False si el factorial es impar.
(3) Método calcular_multiples(*numeros)

Debe recibir varios números y retornar un diccionario donde:

La clave sea el número.
El valor sea su factorial."""
class FactorialFinder:
    def calcular_factorial(self, numero):
        resultado = 1
        for i in range(1, numero + 1):
            resultado = resultado * i
        return resultado

    def es_factorial_par(self, numero):
        factorial = self.calcular_factorial(numero)
        return factorial % 2 == 0

    def calcular_multiples(self, *numeros):
        resultados = {}
        for numero in numeros:
            resultados[numero] = self.calcular_factorial(numero)
        return resultados

factorial = FactorialFinder()
print(factorial.calcular_factorial(5))
print(factorial.es_factorial_par(4))
print(factorial.calcular_multiples(3, 4, 5, 6))