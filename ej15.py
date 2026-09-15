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